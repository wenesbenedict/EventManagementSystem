SFE PRACTICUM CODE EXTRACT

Source: the uploaded SFE Practicum 1–12 documents.

Included code:
- Practicum 7: Event Management System + 19 Pytest tests
- Practicum 8: Ticket pricing function + equivalence partitioning tests + boundary value tests
- Practicum 11: Menu-driven software metrics program
- Practicum 12: Basic COCOMO estimator

No source-code listing was present in the uploaded Practicum 9 or Practicum 10 documents:
- Practicum 9 describes Selenium automation test preparation and execution, but does not provide a Selenium script.
- Practicum 10 describes a DevOps pipeline design and tools, but does not provide a GitHub Actions YAML workflow or Dockerfile.

Practicums 1–6 are documentation/UML diagram tasks and contain no program code.

Formatting note:
The source documents contain broken/misaligned indentation in some code blocks due to document formatting. Indentation was normalized so the extracted Python programs are executable. The program logic and values were retained from the documents; no new Selenium or DevOps code was invented.

Run instructions:
1. Install Python.
2. For Practicum 7 and 8, install pytest:
   pip install pytest
3. Open a terminal in the relevant practicum folder.
4. Run tests:
   python -m pytest -v
5. For Practicum 11 and 12:
   python software_metrics.py
   python basic_cocomo.py

Practicum 10 - DevOps Pipeline
==============================

The root `.github/workflows/ci.yml` workflow runs on every push and pull
request. It installs Python dependencies, runs the Practicum 7 and 8 Pytest
tests, starts the Practicum 9 Flask application, runs its Selenium tests,
uploads JUnit XML results and application logs, and stops the application.
The Docker image is built only when both test jobs succeed. The workflow does
not deploy to production.

Local test commands (PowerShell)
--------------------------------

From the project root:

    py -m venv .venv
    .\.venv\Scripts\python.exe -m pip install --upgrade pip
    .\.venv\Scripts\python.exe -m pip install pytest
    .\.venv\Scripts\python.exe -m pytest -v Practicum_07_White_Box
    .\.venv\Scripts\python.exe -m pytest -v Practicum_08_Black_Box

Install the Practicum 9 requirements before running the browser tests:

    .\.venv\Scripts\python.exe -m pip install -r Practicum_09_Automation_Testing\requirements.txt

In a first PowerShell terminal, start the application:

    Set-Location Practicum_09_Automation_Testing
    ..\.venv\Scripts\python.exe app.py

In a second PowerShell terminal, run the Selenium tests:

    Set-Location Practicum_09_Automation_Testing
    ..\.venv\Scripts\python.exe -m pytest -v test_eventsphere_registration.py

A Chrome/Chromium browser must be installed locally. Selenium Manager
automatically obtains a compatible driver when network access is available.

Docker commands
---------------

From the project root:

    docker build -t eventsphere:local .
    docker run --rm -p 5000:5000 eventsphere:local

Open `http://127.0.0.1:5000/events` while the container is running.

Push the project to GitHub
--------------------------

Create an empty repository named `EventManagementSystem` on GitHub, then run
these commands from the project root. Replace `<GITHUB_USERNAME>` with the
account that owns the repository:

    git init
    git add .
    git commit -m "Add Practicum 10 DevOps pipeline"
    git branch -M main
    git remote add origin https://github.com/<GITHUB_USERNAME>/EventManagementSystem.git
    git push -u origin main

If a remote named `origin` already exists, use this instead of `git remote
add origin`:

    git remote set-url origin https://github.com/<GITHUB_USERNAME>/EventManagementSystem.git

Verify the pipeline
-------------------

After pushing, open the repository on GitHub and select the **Actions** tab.
Open the **EventSphere CI** workflow run for the push. Confirm that
**Practicum 7 and 8 tests** and **Practicum 9 Selenium tests** are green before
the **Build EventSphere Docker image** job starts. The run is successful only
when all three jobs are green. Test reports and the application log are
available under the run's **Artifacts** section.
