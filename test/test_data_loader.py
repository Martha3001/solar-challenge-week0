import pytest
import pandas as pd
import os
import sys
module_path = os.path.abspath(os.path.join('..'))
if module_path not in sys.path:
    sys.path.append(module_path)
    
from src.data_loader import DataLoader

def test_load_csv(tmp_path):
    # Create a temporary CSV file
    test_data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
    file_path = tmp_path / "test.csv"
    test_data.to_csv(file_path, index=False)
    
    # Test loading
    loaded = DataLoader.load_csv(file_path)
    pd.testing.assert_frame_equal(loaded, test_data)
