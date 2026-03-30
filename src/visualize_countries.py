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

import matplotlib.ticker as mticker

def top_n_with_other(names, values, n=10):
    # Sort by value descending
    sorted_data = sorted(zip(names, values), key=lambda x: x[1], reverse=True)
    top = sorted_data[:n]
    other = sorted_data[n:]
    top_names = [name for name, _ in top]
    top_values = [val for _, val in top]
    if other:
        other_value = sum(val for _, val in other)
        top_names.append('Other')
        top_values.append(other_value)
    return top_names, top_values

def create_pie_chart(names, values, title, colors):
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(values, labels=names, autopct='%1.1f%%', startangle=140, colors=colors)
    ax.set_title(title)
    return fig

def create_bar_chart(names, values, title, ylabel, color):
    fig, ax = plt.subplots(figsize=(10, 6))
    bars = ax.bar(names, values, color=color)
    ax.set_title(title)
    ax.set_xlabel('Country')
    ax.set_ylabel(ylabel)
    ax.set_xticklabels(names, rotation=45, ha='right')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}' if x >= 1 else str(x)))
    fig.tight_layout()
    return fig

def create_scatter_plot(areas, populations, country_names):
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(areas, populations, color='teal', alpha=0.7, edgecolor='k')
    ax.set_title('Country Area vs Population (Log Scale, Top 10 Annotated)')
    ax.set_xlabel('Area (sq km)')
    ax.set_ylabel('Population')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.grid(True, which='both', ls='--', lw=0.5)
    # Format axes with thousands separators
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}' if x >= 1 else str(x)))
    ax.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f'{int(x):,}' if x >= 1 else str(x)))
    # Annotate top 10 countries by population
    top_n = 10
    sorted_idx = sorted(range(len(populations)), key=lambda i: populations[i], reverse=True)[:top_n]
    for i in sorted_idx:
        ax.annotate(country_names[i], (areas[i], populations[i]), textcoords="offset points", xytext=(5,5), ha='left', fontsize=8, color='darkred')
    fig.tight_layout()
    return fig

def create_country_plots(country_names, areas, populations):
    """
    Takes three lists (country_names, areas, populations) and returns three matplotlib Figure objects:
    - Area pie chart (top 10 + Other)
    - Population bar chart (top 10)
    - Area vs Population scatter plot (log scale, annotated)
    """
    figs = []
    # Area pie chart
    area_names, area_values = top_n_with_other(country_names, areas)
    figs.append(create_pie_chart(area_names, area_values, 'Area Distribution by Country (Top 10 + Other)', plt.cm.Paired.colors))
    # Population bar chart
    pop_sorted = sorted(zip(country_names, populations), key=lambda x: x[1], reverse=True)
    bar_names = [name for name, _ in pop_sorted[:10]]
    bar_values = [val for _, val in pop_sorted[:10]]
    figs.append(create_bar_chart(bar_names, bar_values, 'Top 10 Countries by Population', 'Population', 'purple'))
    # Scatter plot
    figs.append(create_scatter_plot(areas, populations, country_names))
    return figs

# Example usage:
if __name__ == "__main__":
    country_names = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E']
    areas = [50000, 75000, 60000, 25000, 90000]
    populations = [1000000, 2000000, 1500000, 500000, 3000000]
    figures = create_country_plots(country_names, areas, populations)
    for fig in figures:
        fig.show()
