import sqlite3
from sqlalchemy import create_all, Table, Column, Integer, String, Float, MetaData

DB_URL = "sqlite:///bank_data.db"

def init_db():
    # Define a schema matching bank loan application data
    conn = sqlite3.connect("bank_data.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS loan_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            applicant_name TEXT NOT NULL,
            loan_amount REAL NOT NULL,
            loan_type TEXT,
            branch TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()