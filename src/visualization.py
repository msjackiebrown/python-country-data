"""
Visualization utilities for country data using Matplotlib.
"""
import matplotlib.pyplot as plt

def plot_sample():
    """Plot a sample bar chart as a template."""
    countries = ['Country A', 'Country B', 'Country C']
    values = [10, 20, 15]
    plt.figure(figsize=(8, 5))
    plt.bar(countries, values, color='skyblue')
    plt.title('Sample Country Data')
    plt.xlabel('Country')
    plt.ylabel('Value')
    plt.tight_layout()
    plt.show()
