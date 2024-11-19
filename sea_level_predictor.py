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
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x_1, y_1)
    x_extend =np.linspace(min(x_1), max(x_1) + 50,100)
    plt.plot(x_extend, slope1*x_extend + intercept1, color='r', label='First line of best fit')
    # Create second line of best fit
    x_2= df[(df['Year'] >= 2000)]['Year']
    y_2= df[(df['Year'] >= 2000)]['CSIRO Adjusted Sea Level']
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_2, y_2)
    x_extend2 =np.linspace(min(x_2), max(x_2) + 50,100)
    plt.plot(x_extend2, slope2*x_extend2 + intercept2, color='c', label='second line of best fit')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
