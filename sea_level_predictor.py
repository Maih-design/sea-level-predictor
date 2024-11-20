import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv', sep=',')
    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # Create first line of best fit
    x_1= df['Year']
    y_1= df['CSIRO Adjusted Sea Level']
    slope1, intercept1, _, _, _ = linregress(x_1, y_1)
    x_extend = np.arange(1880, 2051)
    plt.plot(x_extend, slope1*x_extend + intercept1, color='r', label='First line of best fit')
    # Create second line of best fit
    x_2= df[(df['Year'] >= 2000)]['Year']
    y_2= df[(df['Year'] >= 2000)]['CSIRO Adjusted Sea Level']
    slope2, intercept2, _, _, _ = linregress(x_2, y_2)
    x_extend2 = np.arange(2000, 2051)
    plt.plot(x_extend2, slope2*x_extend2 + intercept2, color='c', label='second line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
