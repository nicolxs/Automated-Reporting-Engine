import pandas as pd
import sqlite3

DB_PATH = "bank_data.db"

def validate_data(df):
    """Apply validation and cleaning rules to the dataframe."""
    # Work on a copy to avoid SettingWithCopyWarning
    df = df.copy()
    
    # Remove rows with missing critical information
    df = df.dropna(subset=['applicant_name', 'loan_amount'])
    
    # Ensure numerical integrity
    df['loan_amount'] = pd.to_numeric(df['loan_amount'], errors='coerce')
    df = df[df['loan_amount'] > 0]
    
    # Add default status if not present
    if 'status' not in df.columns:
        df['status'] = 'approved'
    
    return df

def clean_and_load(file_path):
    """Extract, transform, and load data from an Excel file into the database."""
    # 1. Extraction
    df = pd.read_excel(file_path)
    
    # 2. Transformation (Validation Layer)
    df = validate_data(df)
    
    # 3. Loading
    conn = sqlite3.connect(DB_PATH)
    df.to_sql('loan_applications', conn, if_exists='append', index=False)
    conn.close()
    return len(df)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        rows = clean_and_load(sys.argv[1])
        print(f"Successfully loaded {rows} rows from {sys.argv[1]}")
    else:
        print("Usage: python processor.py <path_to_excel_file>")