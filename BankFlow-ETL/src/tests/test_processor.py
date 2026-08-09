import pytest
import pandas as pd
from processor import validate_data, clean_and_load
import os
import tempfile

def test_validation_logic():
    """Test that validation removes invalid rows."""
    # Create a dummy "messy" dataframe
    data = {
        'applicant_name': ['Nixon', None, 'Valid User'],
        'loan_amount': [5000, 1000, -50]  # One valid, one missing name, one negative
    }
    df = pd.DataFrame(data)
    
    # Run the validation logic
    df_cleaned = validate_data(df)
    
    # Assertions - only the first row should remain (valid name and positive amount)
    assert len(df_cleaned) == 1
    assert df_cleaned.iloc[0]['applicant_name'] == 'Nixon'
    assert df_cleaned.iloc[0]['loan_amount'] == 5000

def test_validate_data_with_missing_values():
    """Test that rows with missing critical fields are removed."""
    data = {
        'applicant_name': ['Alice', 'Bob', None, 'David'],
        'loan_amount': [1000, None, 3000, 4000],
        'loan_type': ['personal', 'auto', 'home', 'business']
    }
    df = pd.DataFrame(data)
    df_cleaned = validate_data(df)
    
    # Alice and David's rows should remain (both have valid name and amount)
    assert len(df_cleaned) == 2
    assert df_cleaned.iloc[0]['applicant_name'] == 'Alice'
    assert df_cleaned.iloc[1]['applicant_name'] == 'David'

def test_validate_data_adds_status():
    """Test that status column is added if not present."""
    data = {
        'applicant_name': ['Test User'],
        'loan_amount': [5000]
    }
    df = pd.DataFrame(data)
    df_cleaned = validate_data(df)
    
    assert 'status' in df_cleaned.columns
    assert df_cleaned.iloc[0]['status'] == 'approved'

def test_validate_data_negative_amount():
    """Test that negative loan amounts are filtered out."""
    data = {
        'applicant_name': ['User1', 'User2', 'User3'],
        'loan_amount': [5000, -100, 0]
    }
    df = pd.DataFrame(data)
    df_cleaned = validate_data(df)
    
    # Only the first row with positive amount should remain
    assert len(df_cleaned) == 1
    assert df_cleaned.iloc[0]['loan_amount'] == 5000