# HRIS App - Frappe/ERPNext Technical Test Submission

This repository contains the custom HRIS application developed for the technical test.


## Setup Instructions

1.  **Clone the FrappeDev environment:**
    ```bash
    git clone [https://github.com/yamenzk/FrappeDev.git](https://github.com/yamenzk/FrappeDev.git)
    cd FrappeDev
    ```
2.  **Launch Docker-based Frappe environment:**
    * Follow the `README.md` inside the `FrappeDev` folder carefully.
    **Run the interactive installer:**
    This script will configure your project, build Docker images, and set up the Frappe development environment.
    ```bash
    ./install.sh
    ```
    ./fh start
    ```

3.  **Install this custom `hris` application:**
    * Go into the running Frappe container: ./fh shell
    * Get the app:
        ```bash
        bench get-app hris [https://github.com/AmhaBK/hris-ERPNext.git](https://github.com/AmhaBK/hris-ERPNext.git)
        ```
    * Install on site: `bench --site dev.localhost install-app hris`
    * Apply database changes: `bench --site dev.localhost migrate`
    * Exit container: `exit`
4.  **Access:** On your web browser: `http://dev.localhost:8000` (Login: `Administrator`/`admin`).


## Implemented Workflow Explanation

A "Leave Request" Doctype has been created with custom fields.
* **Backend Logic (Python):** Automatically calculates `total_days` and validates the employee's annual leave balance (max 30 days/year). An error is raised if the limit is exceeded.
* **Frontend Behavior (JavaScript):** Automatically calculates and displays `total_days` on the form. If `total_days` exceeds 15, an informational message prompts confirmation with HR.
* **Approval Workflow:**
    * Employee creates a "Leave Request" (status: Draft).
    * Employee submits the request (status: Submitted).
    * HR Manager can then "Approve" (status: Approved) or "Reject" (status: Rejected) the submitted request.


