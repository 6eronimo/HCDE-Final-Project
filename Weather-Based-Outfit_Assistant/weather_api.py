import requests
from key import WEATHERSTACK_API_KEY  # Import the API key from key.py


def get_weather(city):
    """
    Weather data for a given city in Fahrenheit.

    Parameteres:
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


# Test function
def test_get_weather():
    city = "Seattle"  # City to test
    try:
        weather_data = get_weather(city)
        print("Weather data retrieved successfully:")
        print(f"City: {weather_data['location']['name']}")
        print(f"Temperature: {weather_data['current']['temperature']}°F")
        print(f"Condition: {weather_data['current']['weather_descriptions'][0]}")
    except Exception as e:
        print(f"Test failed: {e}")


if __name__ == "__main__":
    test_get_weather()