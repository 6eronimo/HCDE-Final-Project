def generate_outfit_recommendation(temperature, weather_conditions):
    """
    Parameters:
        temperature (int): The current temperature in Fahrenheit.
        weather_conditions (str): Description of the current weather.

    Returns:
        str: Outfit recommendation
    """
    recommendation = ""  # Initialize an empty string for the outfit recommendation.

    # Temperature-based recommendations (in Fahrenheit).
    # Different suggestions are provided based on the temperature ranges.
    if temperature < 50:
        # Cold weather: Suggest wearing warm clothing like a coat and gloves.
        recommendation = "Not going to lie, it's cold out there. Better wear a warm coat, and gloves."
    elif 50 <= temperature < 68:
        # Chilly weather: Suggest wearing a jacket or sweater for comfort.
        recommendation = "Hmm, a bit chilly today. A jacket or sweater will keep you comfy."
    else:
        # Warm weather: Suggest light clothing like a t-shirt.
        recommendation = "A t-shirt should do just fine."

    # Weather condition-specific advice.
    # Add additional recommendations based on the weather description.
    if "rain" in weather_conditions.lower():
        # If it's rainy, suggest carrying an umbrella.
        recommendation += " Oh, and don't forget an umbrella. Trust me, you'll thank me later."
    elif "snow" in weather_conditions.lower():
        # If it's snowy, suggest boots and a heavy coat.
        recommendation += " It's snowy, so boots and a heavy coat are a must."
    elif "sun" in weather_conditions.lower():
        # If it's sunny, suggest sunglasses and sunscreen for protection.
        recommendation += " It's sunny out so grab some shades and sunscreen."

    # Friendly closing statement to end the recommendation.
    recommendation += " Lock in and own the day!"
    return recommendation