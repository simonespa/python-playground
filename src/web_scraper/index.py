import requests
from bs4 import BeautifulSoup

# URL of BBC Sounds homepage
url = "https://www.bbc.co.uk/sounds/stations"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content of the page
soup = BeautifulSoup(response.text, 'html.parser')

stations = soup.find_all('a', attrs={"data-bbc-source": True})

# stations = [station.get('href').split('/')[-1] for station in stations]
stations = [station.get('data-bbc-source') for station in stations]

print(stations)
