from fastapi import FastAPI, Depends
from app.db import get_conn

app = FastAPI(title="AI Jobs API - Stage 3")

@app.get("/")
def home():
    """Confirma que la API está viva."""
    return {"status": "success", "message": "API Conectada y Columnas Ajustadas"}

@app.get("/jobs")
def list_jobs(conn=Depends(get_conn)):
    cur = conn.cursor()
    try:
        # Aplicamos comillas dobles a "Job Title", "Company Name" y "Location"
        cur.execute(
            """
            SELECT j."Job Title", c."Company Name", j."Location"
            FROM jobs j
            JOIN companies c ON j.company_id = c.company_id
            LIMIT 10;
            """
        )
        return cur.fetchall()
    except Exception as e:
        return {"error_type": "Database Error", "details": str(e)}
    finally:
        cur.close()

@app.get("/kpi/demand-by-location")
def get_demand(conn=Depends(get_conn)):
    cur = conn.cursor()
    try:
        # Ajustado a "Location" y "Job Id" según el error anterior
        cur.execute(
            """
            SELECT "Location", COUNT("job_id") as total
            FROM jobs
            GROUP BY "Location"
            ORDER BY total DESC
            LIMIT 5;
            """
        )
        return cur.fetchall()
    except Exception as e:
        return {"error": str(e)}
    finally:
        cur.close()
        
@app.get("/kpi/top-hiring-companies")
def get_top_companies(conn=Depends(get_conn)):
    cur = conn.cursor()
    try:
        # SQL para contar vacantes por empresa usando el JOIN correcto
        cur.execute(
            """
            SELECT c."Company Name", COUNT(j.job_id) as total_jobs
            FROM companies c
            JOIN jobs j ON c.company_id = j.company_id
            GROUP BY c."Company Name"
            ORDER BY total_jobs DESC
            LIMIT 5;
            """
        )
        return cur.fetchall()
    except Exception as e:
        return {"error": str(e)}
    finally:
        cur.close()