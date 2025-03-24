import os

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "joshua4christ7")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_HOST = os.getenv("DB_HOST", "database-1.cxs64eo44osy.ap-south-1.rds.amazonaws.com")
DB_NAME = os.getenv("DB_NAME", "college_registration")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"