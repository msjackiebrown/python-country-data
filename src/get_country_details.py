"""
get_country_details.py
---------------------
Fetches and parses country details (name, population, area) from a sample website.
This script is adapted from the learning notebook for use as a reusable Python module.
"""
import requests
from bs4 import BeautifulSoup

def get_country_details(url="https://www.scrapethissite.com/pages/simple/"):
    """
    Fetch country details from the given URL.
    Returns three lists: country_names, country_populations, country_areas.
    """
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    countries = soup.find_all('div', class_='col-md-4 country')

    country_names = []
    country_populations = []
    country_areas = []

    for country in countries:
        # Extract and clean the country name from the <h3> tag
        name = country.find('h3').text.strip()
        # Extract and clean the population from the <span class='country-population'> tag
        population = country.find('span', class_='country-population').text.strip()
        # Extract and clean the area from the <span class='country-area'> tag
        area = country.find('span', class_='country-area').text.strip()
        
        country_names.append(name)
        country_populations.append(population)
        country_areas.append(area)

    return country_names, country_populations, country_areas

if __name__ == "__main__":
    names, populations, areas = get_country_details()
    for n, p, a in zip(names, populations, areas):
        print(f"Country: {n}, Population: {p}, Area: {a}")
