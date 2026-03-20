import pandas as pd
import sqlite3

def clean_and_load(file_path):
    # 1. Extraction
    df = pd.read_excel(file_path) [cite: 185]
    
    # 2. Transformation (Validation Layer)
    # Remove rows with missing critical information
    df = df.dropna(subset=['applicant_name', 'loan_amount'])
    
    # Ensure numerical integrity
    df['loan_amount'] = pd.to_numeric(df['loan_amount'], errors='coerce')
    df = df[df['loan_amount'] > 0]
    
    # 3. Loading
    conn = sqlite3.connect("bank_data.db") [cite: 186]
    df.to_sql('loan_records', conn, if_exists='append', index=False)
    conn.close()
    return len(df)