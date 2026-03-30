"""
main.py
-------
Entry point for the country data visualization project.
Fetches country details and visualizes them using Matplotlib.
"""
from get_country_details import get_country_details
from visualize_countries import create_country_plots

if __name__ == "__main__":
    # Fetch country data from the website
    country_names, populations, areas = get_country_details()

    # Convert populations and areas to integers/floats if needed
    populations = [int(p.replace(",", "")) for p in populations]
    areas = [float(a.replace(",", "")) for a in areas]

    # Create plots
    figures = create_country_plots(country_names, areas, populations)

    # Show plots
    for fig in figures:
        fig.show()
