import requests
from key import WEATHERSTACK_API_KEY  # Weatherstack API key
from key import IPINFO_API_KEY     # ipinfo.io API key

def get_location():
    """
    Fetch the user's city using the ipinfo.io API.

    Returns:
        str: The detected city name.
    """
    url = f"https://ipinfo.io?token={IPINFO_API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data['city']
    else:
        raise Exception(f"Error fetching location: {response.status_code}")

def get_weather(city):
    """
    Fetch weather data for a given city in Fahrenheit.

    Parameters:
        city (str): The name of the city.

    Returns:
        dict: Weather data retrieved from the Weatherstack API.
    """
    url = f"http://api.weatherstack.com/current?access_key={WEATHERSTACK_API_KEY}&query={city}&units=f"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "current" in data:
            return data
        else:
            raise Exception("No weather data found in the response.")
    else:
        raise Exception(f"Error fetching weather data: {response.status_code}")