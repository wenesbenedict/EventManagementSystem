FROM python:3.12-slim

WORKDIR /app

COPY Practicum_09_Automation_Testing/requirements.txt ./requirements.txt
RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

COPY Practicum_09_Automation_Testing/app.py ./app.py

ENV PYTHONUNBUFFERED=1
EXPOSE 5000

# Use Flask's host option so the application is reachable through Docker port mapping.
CMD ["flask", "--app", "app", "run", "--host=0.0.0.0", "--port=5000"]
