import numpy as np
import pandas as pd
from scipy import stats

class DataCleaner:
    """Handles cleaning and preprocessing of solar data"""
    
    @staticmethod
    def clip_negative_values(df, columns):
        """
        Clip negative values to 0 in specified columns
        Args:
            df: DataFrame to clean
            columns: List of columns to process
        Returns:
            Cleaned DataFrame
        """
        df[columns] = df[columns].clip(lower=0)
        return df
    
    @staticmethod
    def handle_outliers(df, numeric_columns, z_threshold=3):
        """
        Detect and handle outliers using Z-score method
        Args:
            df: DataFrame to process
            numeric_columns: List of numeric columns to check
            z_threshold: Z-score threshold for outliers
        Returns:
            Tuple of (cleaned DataFrame, number of outliers found)
        """
        z_scores = np.abs(stats.zscore(df[numeric_columns]))
        outlier_flags = (z_scores > z_threshold).any(axis=1)
        outlier_count = outlier_flags.sum()
        
        for col in numeric_columns:
            df.loc[outlier_flags, col] = df[col].median()
            
        return df, outlier_count
    