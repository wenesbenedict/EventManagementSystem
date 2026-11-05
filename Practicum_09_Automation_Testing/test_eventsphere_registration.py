"""
Practicum 9 - Automation Testing using Selenium + Pytest

Before running:
1. Start the EventSphere web application.
2. Set EVENTSPHERE_URL to the registration page URL.
3. Add the data-testid attributes used below to the matching UI elements,
   OR change the selectors to match your actual frontend.
4. Set TEST_EMAIL to an email accepted by your test environment.

Expected UI contract (adapt selectors to your app):
  attendee-name, attendee-email, attendee-phone, event-select,
  register-button, registration-success, validation-error,
  ticket-qr, duplicate-error
"""
import os
import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "http://127.0.0.1:5000/events"
WAIT_SECONDS = 10

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(options=options)  # Selenium Manager handles driver
    browser.set_window_size(1365, 900)
    yield browser
    browser.quit()

def find(driver, test_id):
    return driver.find_element(By.CSS_SELECTOR, f'[data-testid="{test_id}"]')

def wait_for(driver, test_id):
    return WebDriverWait(driver, WAIT_SECONDS).until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f'[data-testid="{test_id}"]')
        )
    )

def fill_registration_form(driver, name, email, phone):
    driver.get(BASE_URL)
    find(driver, "attendee-name").clear()
    find(driver, "attendee-name").send_keys(name)
    find(driver, "attendee-email").clear()
    find(driver, "attendee-email").send_keys(email)
    find(driver, "attendee-phone").clear()
    find(driver, "attendee-phone").send_keys(phone)

    # If your page has an event dropdown, select the first available event.
    event_select = driver.find_element(
        By.CSS_SELECTOR, '[data-testid="event-select"]'
    )
    Select(event_select).select_by_index(1)

def test_successful_registration_generates_ticket(driver):
    unique_email = f"selenium_{uuid.uuid4().hex[:8]}@example.com"
    fill_registration_form(driver, "Test Attendee", unique_email, "9876543210")
    find(driver, "register-button").click()

    wait_for(driver, "registration-success")
    # FR-8: successful registration should produce a digital ticket / QR code.
    wait_for(driver, "ticket-qr")

def test_invalid_email_is_rejected(driver):
    fill_registration_form(driver, "Test Attendee", "not-an-email", "9876543210")
    find(driver, "register-button").click()

    # The UI should display a validation message and not a success state.
    wait_for(driver, "validation-error")
    assert not driver.find_elements(
        By.CSS_SELECTOR, '[data-testid="registration-success"]'
    )

def test_missing_name_is_rejected(driver):
    fill_registration_form(driver, "", f"missing_{uuid.uuid4().hex[:8]}@example.com",
                           "9876543210")
    find(driver, "register-button").click()
    wait_for(driver, "validation-error")

def test_duplicate_registration_is_prevented(driver):
    email = f"duplicate_{uuid.uuid4().hex[:8]}@example.com"

    # First registration
    fill_registration_form(driver, "Test Attendee", email, "9876543210")
    find(driver, "register-button").click()
    wait_for(driver, "registration-success")

    # Attempt the same registration again
    fill_registration_form(driver, "Test Attendee", email, "9876543210")
    find(driver, "register-button").click()
    wait_for(driver, "duplicate-error")
