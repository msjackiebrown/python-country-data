"""
main.py
-------
Entry point for the country data visualization project.
Fetches country details and visualizes them using Matplotlib.
"""
from get_country_details import get_country_details
from visualize_countries import create_country_plots

if __name__ == "__main__":
    print("Fetching country data from the web...")
    country_names, populations, areas = get_country_details()

    # Convert populations and areas to integers/floats if needed
    populations = [int(p.replace(",", "")) for p in populations]
    areas = [float(a.replace(",", "")) for a in areas]

    print("Creating Matplotlib plots...")
    figures = create_country_plots(country_names, areas, populations)

    print("\nDisplaying plots. Each plot will open in a new window.")
    print("You can interact with the plot window: zoom, pan, or save the figure using the toolbar.")
    print("Close each window to continue to the next plot (if multiple).\n")

    # Show plots interactively
    for i, fig in enumerate(figures, 1):
        print(f"Showing plot {i} of {len(figures)}...")
        fig.show()
    print("All plots displayed. Exiting.")
