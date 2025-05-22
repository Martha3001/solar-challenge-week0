import pytest
import pandas as pd
import numpy as np
import os
import sys

# Add parent directory to sys.path BEFORE imports
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)

from src.data_cleaner import DataCleaner 

@pytest.fixture
def sample_data():
    return pd.DataFrame({
        'A': [1, 2, -3, 4, 1000],
        'B': [5, -6, 7, 8, 9],
        'C': [-10, 11, 12, 13, 14]
    })

def test_clip_negative_values(sample_data):
    cleaned = DataCleaner.clip_negative_values(sample_data, ['A', 'B', 'C'])
    assert (cleaned['A'] >= 0).all()
    assert (cleaned['B'] >= 0).all()
    assert (cleaned['C'] >= 0).all()
    assert cleaned.loc[0, 'A'] == 1  # Positive value unchanged
    assert cleaned.loc[2, 'A'] == 0  # Negative value clipped

def test_handle_outliers(sample_data):
    cleaned, count = DataCleaner.handle_outliers(sample_data, ['A', 'B', 'C'], z_threshold=2)
    assert count == 1  # Only the 1000 in column A should be an outlier
    assert cleaned.loc[4, 'A'] == np.median(sample_data['A'])  # Outlier replaced with median
