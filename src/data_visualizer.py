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