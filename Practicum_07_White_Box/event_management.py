class EventManagementSystem:
    def __init__(self):
        self.events = {
            "Tech Fest": {
                "capacity": 100,
                "registered": 60,
                "price": 500
            },
            "Music Fest": {
                "capacity": 50,
                "registered": 50,
                "price": 800
            },
            "Workshop": {
                "capacity": 30,
                "registered": 15,
                "price": 300
            }
        }

    def login(self, username, password):
        if username == "admin" and password == "admin123":
            return "Login Successful"
        elif username == "user" and password == "user123":
            return "Login Successful"
        else:
            return "Invalid Username or Password"

    def check_availability(self, event_name):
        if event_name not in self.events:
            return "Event Not Found"
        event = self.events[event_name]
        if event["registered"] < event["capacity"]:
            available = event["capacity"] - event["registered"]
            return f"Event Available - {available} seats remaining"
        else:
            return "Event Full"

    def register(self, event_name, participant_name):
        if event_name not in self.events:
            return "Event Not Found"
        if participant_name == "":
            return "Participant Name Required"
        event = self.events[event_name]
        if event["registered"] >= event["capacity"]:
            return "Registration Failed - Event Full"
        event["registered"] += 1
        return "Registration Successful"

    def calculate_cost(self, event_name, members):
        if event_name not in self.events:
            return 0
        if members <= 0:
            return 0
        price = self.events[event_name]["price"]
        total = price * members
        if members >= 5:
            total = total * 0.90
        return total

    def payment(self, amount, payment_status):
        if amount <= 0:
            return "Invalid Amount"
        if payment_status == "success":
            return "Payment Successful"
        else:
            return "Payment Failed"

    def confirm_booking(self, registration_status, payment_status):
        if registration_status == "Registration Successful":
            if payment_status == "Payment Successful":
                return "Booking Confirmed"
            else:
                return "Booking Failed - Payment Unsuccessful"
        else:
            return "Booking Failed - Registration Unsuccessful"
