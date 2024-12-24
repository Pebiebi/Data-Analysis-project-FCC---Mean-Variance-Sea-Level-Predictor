import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data['Year'], data['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    slope, intercept, _, _, _ = linregress(data['Year'], data['CSIRO Adjusted Sea Level'])
    
    years_extended = range(1880, 2051)
    sea_levels_extended = [slope * year + intercept for year in years_extended]
    
    plt.plot(years_extended, sea_levels_extended, label='Fit All Data')

    # Create second line of best fit
    data_recent = data[data['Year'] >= 2000]

    slope_recent, intercept_recent, _, _, _ = linregress(data_recent['Year'], data_recent['CSIRO Adjusted Sea Level'])

    years_recent_extended = range(2000, 2051)
    sea_levels_recent_extended = [slope_recent * year + intercept_recent for year in years_recent_extended]

    plt.plot(years_recent_extended, sea_levels_recent_extended, label='Fit from 2000', color='red')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Show the legend
    plt.legend()

    # Show the plot
    plt.show()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()