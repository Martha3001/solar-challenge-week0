import seaborn as sns
import matplotlib.pyplot as plt
from windrose import WindroseAxes

class DataVisualizer:
    """Handles visualization of solar data"""
    
    @staticmethod
    def plot_daily_patterns(df, solar_cols=['GHI', 'DNI', 'DHI'], temp_col='Tamb'):
        """Plot daily patterns of solar radiation and temperature"""
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 8))
        
        # Solar metrics
        for col in solar_cols:
            sns.lineplot(data=df, x='Hour', y=col, label=col, ax=ax1)
        ax1.set_title('Average Hourly Solar Radiation')
        ax1.set_ylabel('W/m²')
        ax1.grid(True)
        
        # Temperature
        sns.lineplot(data=df, x='Hour', y=temp_col, color='red', label='Ambient Temp', ax=ax2)
        ax1.set_title('Average Hourly Temperatures')
        ax1.set_ylabel('°C')
        ax1.grid(True)
        
        plt.tight_layout()
        return fig
    
    @staticmethod
    def plot_wind_rose(df, wind_dir_col='WD', wind_speed_col='WS'):
        """Create wind rose plot"""
        fig = plt.figure(figsize=(8, 8))
        ax = WindroseAxes.from_ax(fig=fig)
        ax.bar(df[wind_dir_col], df[wind_speed_col], normed=True, opening=0.8, edgecolor='white')
        ax.set_legend()
        plt.title("Wind Rose: Wind Speed vs Wind Direction")
        return fig
    
    @staticmethod
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

    @staticmethod
    def plot_ghi_ranking(df):
        """
        Create a bar plot ranking countries by average GHI.
        """
        avg_ghi = df.groupby('Country')['GHI'].mean().sort_values(ascending=False)
        fig = plt.figure(figsize=(6, 4))
        avg_ghi.plot(kind='bar', color=['#1f77b4', '#ff7f0e', '#2ca02c'])
        plt.title('Average GHI by Country')
        plt.ylabel('GHI (kWh/m²/day)')
        plt.xlabel('Country')
        plt.xticks(rotation=0)
        plt.tight_layout()

        return fig

