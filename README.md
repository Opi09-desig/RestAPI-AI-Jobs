# AI Jobs Market Analysis API 🚀

## Overview
This project is a REST API developed with **FastAPI** to analyze the job market for Artificial Intelligence and Data Engineering in the United States. It connects to a **PostgreSQL** relational database to provide real-time metrics (KPIs) about hiring trends, top locations, and salary distributions.

## Architecture & Data Model
The system is built upon a relational schema with three core entities:
* **Jobs**: Contains position titles, salary estimates, and descriptions.
* **Companies**: Stores employer details, industry, and headquarters information.
* **Skills**: Maps specific technical requirements to each job posting.

## Tech Stack
* **Language**: Python 3.13
* **Framework**: FastAPI
* **Database**: PostgreSQL
* **Database Driver**: Psycopg (using `dict_row` for JSON responses)

## Key Features & Endpoints
The API exposes several endpoints to extract business intelligence:
- `GET /jobs`: Lists the first 10 available job entries.
- `GET /kpi/demand-by-location`: Identifies cities with the highest job density.
- `GET /kpi/top-hiring-companies`: Ranks the top 5 companies currently hiring.

## Installation

1. **Environment Variables**: Configure your `.env` file with the following keys:
   ```env
   DB_HOST=localhost
   DB_PORT=5432
   DB_NAME=ai_jobs_db
   DB_USER=postgres
   DB_PASSWORD=your_password

2. Run Server:
    python -m uvicorn app.main:app --reload

Endpoints Principales
**GET /jobs: Lista los primeros 10 empleos disponibles.**
**GET /kpi/demand-by-location: Ciudades con mayor demanda de Data Engineers.**
**GET /kpi/top-hiring-companies: Empresas con más vacantes publicadas.**