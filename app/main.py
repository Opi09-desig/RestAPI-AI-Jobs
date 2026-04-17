from fastapi import FastAPI, Depends
from app.settings import APP_NAME, IS_MYSQL
from app.db import get_conn

app = FastAPI(title=APP_NAME)


@app.get("/clients")
def list_clients(conn=Depends(get_conn)):
    if IS_MYSQL:
        cur = conn.cursor(dictionary=True)
    else:
        cur = conn.cursor()

    try:
        cur.execute(
            """
            SELECT client_id, full_name, email, created_at
            FROM clients
            ORDER BY client_id
            LIMIT 10;
            """
        )
        rows = cur.fetchall()
        return rows
    finally:
        cur.close()