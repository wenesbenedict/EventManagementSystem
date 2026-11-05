from event_management import EventManagementSystem


def test_login_valid_admin():
    ems = EventManagementSystem()
    assert ems.login("admin", "admin123") == "Login Successful"


def test_login_invalid_password():
    ems = EventManagementSystem()
    assert ems.login("admin", "wrong123") == "Invalid Username or Password"


def test_login_valid_user():
    ems = EventManagementSystem()
    assert ems.login("user", "user123") == "Login Successful"


def test_event_availability():
    ems = EventManagementSystem()
    assert ems.check_availability("Tech Fest") == "Event Available - 40 seats remaining"


def test_event_full():
    ems = EventManagementSystem()
    assert ems.check_availability("Music Fest") == "Event Full"


def test_event_not_found():
    ems = EventManagementSystem()
    assert ems.check_availability("Unknown Event") == "Event Not Found"


def test_registration_successful():
    ems = EventManagementSystem()
    assert ems.register("Tech Fest", "Vishal") == "Registration Successful"


def test_registration_empty_name():
    ems = EventManagementSystem()
    assert ems.register("Tech Fest", "") == "Participant Name Required"


def test_registration_unknown_event():
    ems = EventManagementSystem()
    assert ems.register("Unknown Event", "Vishal") == "Event Not Found"


def test_cost_calculation_normal():
    ems = EventManagementSystem()
    assert ems.calculate_cost("Tech Fest", 2) == 1000


def test_cost_calculation_discount():
    ems = EventManagementSystem()
    assert ems.calculate_cost("Tech Fest", 5) == 2250.0


def test_cost_unknown_event():
    ems = EventManagementSystem()
    assert ems.calculate_cost("Unknown Event", 2) == 0


def test_cost_zero_members():
    ems = EventManagementSystem()
    assert ems.calculate_cost("Tech Fest", 0) == 0


def test_payment_successful():
    ems = EventManagementSystem()
    assert ems.payment(1000, "success") == "Payment Successful"


def test_payment_failed():
    ems = EventManagementSystem()
    assert ems.payment(1000, "failed") == "Payment Failed"


def test_payment_invalid_amount():
    ems = EventManagementSystem()
    assert ems.payment(0, "success") == "Invalid Amount"


def test_booking_confirmed():
    ems = EventManagementSystem()
    assert ems.confirm_booking(
        "Registration Successful",
        "Payment Successful"
    ) == "Booking Confirmed"


def test_booking_payment_failed():
    ems = EventManagementSystem()
    assert ems.confirm_booking(
        "Registration Successful",
        "Payment Failed"
    ) == "Booking Failed - Payment Unsuccessful"


def test_booking_registration_failed():
    ems = EventManagementSystem()
    assert ems.confirm_booking(
        "Registration Failed",
        "Payment Successful"
    ) == "Booking Failed - Registration Unsuccessful"
