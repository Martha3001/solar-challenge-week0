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
    
    def boxplots_by_country(df, columns = ['GHI', 'DNI', 'DHI']):
        """
        Create side-by-side boxplots for given columns, grouped by a categorical column (e.g., country).
        
        Parameters:
            df (pd.DataFrame): Input DataFrame with at least 'Country' and the specified columns.
            columns (list): List of column names to plot as boxplots.
        
        Returns:
            matplotlib.figure.Figure: The figure containing the subplots.
        """
        fig, axs = plt.subplots(1, len(columns), figsize=(6 * len(columns), 6))

        # Handle single axis case (if len(columns) == 1)
        if len(columns) == 1:
            axs = [axs]

        for i, col in enumerate(columns):
            sns.boxplot(data=df, x='Country', y=col, hue='Country', ax=axs[i], palette='Set2')
            axs[i].set_title(f'{col} by Country')
            axs[i].set_ylabel(f'{col} (W/m²)')
            axs[i].set_xlabel('')

        plt.tight_layout()
        return fig