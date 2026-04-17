import pandas as pd
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()

def migration():
    # Conexión
    engine = create_engine(f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}")
    
    print("🚀 Cargando y limpiando datos...")
    df = pd.read_csv('data/DataEngineer.csv')
    df.replace(["-1", -1], "Unknown", inplace=True) # Limpieza de Stage 1
    
    # Normalización (Tus 2 tablas)
    companies = df[['Company Name', 'Rating', 'Industry', 'Sector', 'Revenue']].drop_duplicates().reset_index(drop=True)
    companies['company_id'] = companies.index + 1
    
    jobs = df.merge(companies[['Company Name', 'company_id']], on='Company Name')
    jobs = jobs[['Job Title', 'Salary Estimate', 'Location', 'Easy Apply', 'company_id']]
    jobs['job_id'] = jobs.index + 1

    # Carga
    companies.to_sql('companies', engine, if_exists='replace', index=False)
    jobs.to_sql('jobs', engine, if_exists='replace', index=False)
    print("✅ ¡Migración completa! Revisa DBeaver.")

if __name__ == "__main__":
    migration()