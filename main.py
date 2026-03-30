"""
main.py
-------
Entry point for the country data visualization project.
Fetches country details and visualizes them using Matplotlib.
"""
from src.get_country_details import get_country_details
from src.visualize_countries import create_country_plots

if __name__ == "__main__":
    
    from src.tk_app import CountryDataApp
    app = CountryDataApp()
    app.mainloop()
