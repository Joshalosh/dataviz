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

    # Make a new varuable, 'counter', from iterating through each
    # line of data in the parsed data, and count how many incidents
    # happen on each day

    # Seperate the x-axis data (the days of the week) from the
    # 'counter' variable from the y-axis data (the number of
    # incidents for each day)

    # With that y-axis data, assign it to a matplotlib plot instance

    # Create the amount of ticks needed for our x-axis, and assign
    # the labels

    # Save the plot!

    # Close plot file


def visualize_type():
    """Visualize data by category in a bar graph"""
    data_file = parse(MY_FILE, ",")
    # Same as before, this returns a dict where it sums the total
    # incidents per Category.
    counter = Counter(item["Category"] for item in data_file)

    # Set the labels which are based on the keys of our counter.
    labels = tuple(counter.keys())

    # Set where the labels hit the x-axis
    xlocations = np.arange(len(labels)) + 0.5

    # Width of each bar
    width = 0.5

    # Assign data to a bar plot
    plt.bar(xlocations, counter.values(), width=width)

    # Assign labels and tick location to x-axis
    plt.xticks(xlocations + width / 2, labels, rotation=90)

    # Give some more room so the labels aren't cut off in the graph
    plt.subplots_adjust(bottom=0.4)

    # Make the overall graph/figure larger
    plt.rcParams['figure.figsize'] = 12, 8

    # Save the graph!
    # If you look at new-coder/dataviz/tutorial_source, you should see
    # the PNG file, "Type.png".  This is our graph!
    plt.savefig("Type.png")

    # Close figure
    plt.clf()


def main():
    visualize_days()
    visualize_type()


if __name__ == "__main__":
    main()
