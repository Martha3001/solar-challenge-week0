import pandas as pd

class DataLoader:
    """Handles loading of solar data from various sources"""
    
    @staticmethod
    def load_csv(filepath):
        """
        Load data from CSV file
        Args:
            filepath: Path to CSV file
        Returns:
            pandas.DataFrame
        """
        return pd.read_csv(filepath)
    
    @staticmethod
    def export_to_csv(dataframe, filepath):
        """
        Export DataFrame to CSV file
        Args:
            dataframe: pandas.DataFrame to export
            filepath: Path to save the CSV file
        """
        dataframe.to_csv(filepath, index=False)