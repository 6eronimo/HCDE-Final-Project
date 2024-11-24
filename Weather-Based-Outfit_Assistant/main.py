from weather_api import get_weather
from outfit_logic import generate_outfit_recommendation

def main():
    print("Hello, I'm FITTZ, your Weather Outfit Assistant Let's get you FITTed.")
    city = input("So, where are you headed today? ")

    try:
        weather_data = get_weather(city)
        temperature = weather_data['current']['temperature']
        weather_conditions = weather_data['current']['weather_descriptions'][0]

        print(f"\nFITTZ: Here's what I found for {city}:")
        print(f"  - Temperature: {temperature}°C")
        print(f"  - Weather: {weather_conditions}")

        outfit_recommendation = generate_outfit_recommendation(temperature, weather_conditions)

        print(f"\nFITTZ: Here's my advice for you:")
        print(f"  {outfit_recommendation}")
    except Exception as e:
        print(f"\nFITTZ: Oops! Something went wrong. Here's the issue: {e}")
        print("FITTZ: Make sure you entered a valid city or check your internet connection.")

if __name__ == "__main__":
    main()