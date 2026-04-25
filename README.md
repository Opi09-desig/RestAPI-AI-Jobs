# AI Jobs Market Intelligence - Stage 4 📊

## Project Overview
This project is a comprehensive market intelligence platform designed to analyze AI job vacancies and salary KPIs. It has evolved into a microservices architecture that integrates a PostgreSQL database, a FastAPI backend, and an interactive Dash frontend.

## Technical Requirements
* **Python:** 3.13+
* **Database:** PostgreSQL (ai_jobs_db)
* **Key Libraries:** * `fastapi` & `uvicorn` (Backend)
    * `dash` & `plotly` (Frontend)
    * `psycopg` & `pandas` (Data Management)

## Project Structure
* `backend_api/`: Contains the FastAPI application and database logic.
* `dash_app/`: Contains the interactive dashboard and visualization components.

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>

2. **Database Configuration**
    Ensure your PostgreSQL server is running and the ai_jobs_db is accessible.
    Configure your .env file with the following credentials:
        DB_NAME=ai_jobs_db
        DB_USER=your_user
        DB_PASSWORD=your_password
        DB_HOST=localhost
        DB_PORT=5432

3. **Install Dependencies:**
    pip install fastapi uvicorn dash dash-bootstrap-components plotly requests pandas psycopg python-dotenv

# Running the Platform
1. **Start the Backend API**
    Navigate to the backend_api directory and run:
        python -m uvicorn app.main:app --reload
        (Swagger UI: Accessible at http://127.0.0.1:8000/docs.)

2. **Start the Dashboard**
    Navigate to the dash_app directory and run:
        python app.py
        (Dashboard URL: Accessible at http://127.0.0.1:8050.)

# Final Results (Stage 4)
    The current version includes a fully functional dashboard with real-time KPI tracking:

    Top Hiring Companies: Interactive bar chart visualizing market leaders.
    Market Share by Location: Donut chart showing geographical job distribution.
    Professional UI: Enhanced with corporate themes and mobile-responsive layouts.