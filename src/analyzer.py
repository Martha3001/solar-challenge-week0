import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SolarAnalyzer:
    """Performs analysis on solar data"""
    
    @staticmethod
    def analyze_cleaning_impact(df, cleaning_col='Cleaning', mod_cols=['ModA', 'ModB']):
        """
        Analyze impact of cleaning on module measurements
        Args:
            df: DataFrame containing the data
            cleaning_col: Column indicating cleaning status
            mod_cols: List of module measurement columns
        Returns:
            Tuple of (grouped DataFrame, matplotlib Figure)
        """
        cleaning_group = df.groupby(cleaning_col)[mod_cols].mean()
        
        fig, ax = plt.subplots(figsize=(8, 5))
        cleaning_group.plot(kind='bar', ax=ax, colormap='viridis')
        ax.set_title("Average Module Measurements Before and After Cleaning")
        ax.set_xlabel("Cleaning Performed (0 = No, 1 = Yes)")
        ax.set_ylabel("Average Irradiance (W/m²)")
        ax.set_xticklabels(['Not Cleaned', 'Cleaned'], rotation=0)
        ax.grid(True, axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        return cleaning_group, fig
    
    @staticmethod
    def calculate_correlations(df, columns):
        """
        Calculate correlation matrix for specified columns
        Args:
            df: DataFrame containing the data
            columns: List of columns to include in correlation
        Returns:
            Correlation matrix DataFrame
        """
        return df[columns].corr()
    
    def calculate_summary_stats(df, columns = ['GHI', 'DNI', 'DHI']):
        """Helper method to compute summary statistics"""
        return df.groupby('Country')[columns].agg(['mean', 'median', 'std'])