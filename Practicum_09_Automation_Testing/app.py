from flask import Flask, request, render_template_string
import qrcode
import io
import base64
import re

app = Flask(__name__)

registered_emails = set()

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>EventSphere - Registration</title>
    <style>
        body {
            font-family: Arial;
            background: #f1f5f9;
            display: flex;
            justify-content: center;
            padding: 40px;
        }
        .container {
            background: white;
            padding: 30px;
            width: 400px;
            border-radius: 12px;
            box-shadow: 0 4px 15px #ccc;
        }
        input, select, button {
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            box-sizing: border-box;
        }
        button {
            background: #2563eb;
            color: white;
            border: none;
            cursor: pointer;
        }
        .success { color: green; }
        .error { color: red; }
        img { display: block; margin: 15px auto; }
    </style>
</head>
<body>
<div class="container">
    <h2>EventSphere Registration</h2>

    <form method="POST" action="/events" novalidate>
        <input data-testid="attendee-name"
               name="name" placeholder="Attendee Name">

        <input data-testid="attendee-email"
               name="email" placeholder="Email">

        <input data-testid="attendee-phone"
               name="phone" placeholder="Phone Number">

        <select data-testid="event-select" name="event">
            <option value="">Select Event</option>
            <option value="Tech Fest">Tech Fest</option>
            <option value="AI Workshop">AI Workshop</option>
        </select>

        <button data-testid="register-button" type="submit">
            Register
        </button>
    </form>

    {% if error == "duplicate" %}
        <p class="error" data-testid="duplicate-error">
            Duplicate registration is not allowed!
        </p>
    {% elif error %}
        <p class="error" data-testid="validation-error">
            {{ error }}
        </p>
    {% endif %}

    {% if success %}
        <div class="success" data-testid="registration-success">
            Registration Successful!
            <p>Your ticket ID: {{ ticket_id }}</p>
        </div>

        <img data-testid="ticket-qr"
             src="data:image/png;base64,{{ qr_code }}"
             width="150">
    {% endif %}
</div>
</body>
</html>
"""

def generate_qr(data):
    qr = qrcode.make(data)
    buffer = io.BytesIO()
    qr.save(buffer, format="PNG")
    return base64.b64encode(buffer.getvalue()).decode()

@app.route("/events", methods=["GET", "POST"])
def register():
    error = None
    success = False
    ticket_id = None
    qr_code = None

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip().lower()
        phone = request.form.get("phone", "").strip()
        event = request.form.get("event", "").strip()

        if not name or not email or not phone or not event:
            error = "All fields are required."

        elif not re.fullmatch(r"[^@\s]+@[^@\s]+\.[^@\s]+", email):
            error = "Invalid email address."

        elif not re.fullmatch(r"\d{10}", phone):
            error = "Phone number must contain 10 digits."

        elif email in registered_emails:
            error = "duplicate"

        else:
            registered_emails.add(email)
            ticket_id = "EVT" + str(len(registered_emails)).zfill(4)
            qr_code = generate_qr(ticket_id + "|" + email + "|" + event)
            success = True

    return render_template_string(
        HTML,
        error=error,
        success=success,
        ticket_id=ticket_id,
        qr_code=qr_code
    )

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)