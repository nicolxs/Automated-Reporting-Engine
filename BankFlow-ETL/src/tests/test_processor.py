import pytest
import pandas as pd
from src.processor import clean_and_load

def test_validation_logic():
    # Create a dummy "messy" dataframe
    data = {
        'applicant_name': ['Nixon', None, 'Valid User'],
        'loan_amount': [5000, 1000, -50] # One valid, one missing name, one negative
    }
    df = pd.DataFrame(data)
    
    # Run your cleaning logic (extract this logic into its own function for testing)
    # df_cleaned = validate_data(df)
    
    # Assertions
    # assert len(df_cleaned) == 1 
    # assert df_cleaned.iloc[0]['applicant_name'] == 'Nixon'