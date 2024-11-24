def generate_outfit_recommendation(temperature, weather_conditions):
    """
    Parameters:
        temperature (int): The current temperature in Fahrenheit.
        weather_conditions (str): Description of the current weather.

    Returns:
        str: Outfit recommendation
    """
    recommendation = ""

    # Temperature-based recommendations (in Fahrenheit)
    if temperature < 50:
        recommendation = "Not going to lie, it's cold out there. Better wear a warm coat, and gloves."
    elif 50 <= temperature < 68:
        recommendation = "Hmm, a bit chilly today. A jacket or sweater will keep you comfy."
    else:
        recommendation = "A t-shirt should do just fine."

    # Weather condition-specific advice
    if "rain" in weather_conditions.lower():
        recommendation += " Oh, and don't forget an umbrella. Trust me, you'll thank me later."
    elif "snow" in weather_conditions.lower():
        recommendation += " It's snowy, so boots and a heavy coat are a must."
    elif "sun" in weather_conditions.lower():
        recommendation += " It's sunny out so grab some shades and sunscreen."

    # Friendly closing statement
    recommendation += " Lock in and own the day!"
    return recommendation