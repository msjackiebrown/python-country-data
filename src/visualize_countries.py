"""
visualize_countries.py
---------------------
This script demonstrates how to visualize country area and population data using Matplotlib.
It creates two bar graphs (area and population by country) and a scatter plot (area vs population).
"""
import matplotlib.pyplot as plt

# Sample data for demonstration
country_names = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
areas = [50000, 75000, 60000, 25000, 90000]
populations = [1000000, 2000000, 1500000, 500000, 3000000]

def create_country_plots(country_names, areas, populations):
    """
    Takes three lists (country_names, areas, populations) and returns three matplotlib Figure objects:
    - Area bar graph
    - Population bar graph
    - Area vs Population scatter plot
    """
    figs = []

    # Area bar graph
    fig1, ax1 = plt.subplots(figsize=(10, 6))
    ax1.bar(country_names, areas, color='orange')
    ax1.set_title('Area by Country')
    ax1.set_xlabel('Country')
    ax1.set_ylabel('Area (sq km)')
    ax1.set_xticklabels(country_names, rotation=45)
    fig1.tight_layout()
    figs.append(fig1)

    # Population bar graph
    fig2, ax2 = plt.subplots(figsize=(10, 6))
    ax2.bar(country_names, populations, color='purple')
    ax2.set_title('Population by Country')
    ax2.set_xlabel('Country')
    ax2.set_ylabel('Population')
    ax2.set_xticklabels(country_names, rotation=45)
    fig2.tight_layout()
    figs.append(fig2)

    # Area vs Population scatter plot
    fig3, ax3 = plt.subplots(figsize=(8, 6))
    ax3.scatter(areas, populations, color='teal')
    ax3.set_title('Country Area vs Population')
    ax3.set_xlabel('Area (sq km)')
    ax3.set_ylabel('Population')
    ax3.grid(True)
    fig3.tight_layout()
    figs.append(fig3)

    return figs

# Example usage:
if __name__ == "__main__":
    country_names = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
    areas = [50000, 75000, 60000, 25000, 90000]
    populations = [1000000, 2000000, 1500000, 500000, 3000000]
    figures = create_country_plots(country_names, areas, populations)
    for fig in figures:
        fig.show()
