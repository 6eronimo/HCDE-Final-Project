from weather_api import get_weather, get_location
from outfit_logic import generate_outfit_recommendation
from html_output import create_html_output

# Main function: orchestrates the process of fetching weather data, generating outfit recommendations,
# and creating an HTML output to display to the user.
def main():
    print("FITTZ: Generating your weather-based outfit recommendations...")

    try:
        # Step 1: Automatically fetch the user's city using IP-based geolocation (via ipinfo.io API).
        city = get_location()  # Fetches city based on user's IP address.
        print(f"FITTZ: Detected your city as {city}.")  # Debugging/logging message to confirm city detection.

        # Step 2: Fetch weather data for the detected city using Weatherstack API.
        # This includes the temperature (in Fahrenheit) and a brief weather description.
        weather_data = get_weather(city)  # Fetch weather details for the city.
        temperature = weather_data['current']['temperature']  # Extract temperature from API response.
        weather_conditions = weather_data['current']['weather_descriptions'][0]  # Extract weather condition description.

        # Step 3: Generate an outfit recommendation based on the temperature and weather conditions.
        # Recommendations consider factors like rain, snow, or sun and provide specific advice.
        outfit_recommendation = generate_outfit_recommendation(temperature, weather_conditions)

        # Step 4: Generate an HTML page to display the weather data and outfit recommendation.
        # The generated HTML uses Bootstrap for styling and ensures readability for the user.
        create_html_output(city, weather_data, outfit_recommendation)
        print("FITTZ: Your HTML page has been created. Open 'output.html' to view it!")  # Confirmation for user.

    except Exception as e:
        # Catch-all error handling to ensure the program does not crash unexpectedly.
        print(f"FITTZ: Something went wrong: {e}")  # Throw error message for debugging purposes.
        print("FITTZ: Please check your internet connection or API credentials.")  # Provide a user-friendly error message.

# Entry point for the program.
# Ensures the main function runs only when the script is executed directly.
if __name__ == "__main__":
    main()