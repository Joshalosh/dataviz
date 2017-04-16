"""
Data Visualization Project

Parse data from an ugly CSV or Excel file, and render it in
JSON-like form, visualize in graphs, and plot on Google Maps.

Part II: Take the data we just parsed and visualize it using popular
Python math libraries.
"""

from collections import Counter
from parse import parse

import csv
import matplotlib.pyplot as plt
import numpy as np


MY_FILE = "../data/sample_sfpd_incident_all.csv"


def visualize_days():
    """Visualize data by day of week"""
    
    # Grab our parsed data that we parsed earlier
    data_file = parse('MY_FILE', ",")

    # Make a new variable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day
    counter = Counter(item['DayOfWeek'] for item in data_file)

    # Seperate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)
    data_list = [
                 counter['Monday'],
                 counter['Tuesday'],
                 counter['Wednesday'],
                 counter['Thursday'],
                 counter['Friday'],
                 counter['Saturday'],
                 counter['Sunday'],
                 ]

    day_tuple = (['Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat', 'Sun'])

    # With that y-axis data, assign it to a matplotlib plot instance
    plt.plot(data_list)
    # Create the amount of ticks needed for our x-axis, and assign
    # the labels
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the plot!
    plt.savefig('Days.png')

    # Close plot file
    plt.clf()


def main():
    visualize_days()


if __name__ == "__main__":
    main()
