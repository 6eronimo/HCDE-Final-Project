def create_html_output(city, weather_data, outfit_recommendation):
    """
    Generates an HTML file to display the weather data and outfit recommendations using Bootstrap.

    Parameters:
        city (str): Name of the city.
        weather_data (dict): Weather data retrieved from the Weatherstack API.
        outfit_recommendation (str): Recommendation generated by generate_outfit_recommendation().
    """
    # Extract weather details from the API response.
    # These details include the current temperature and weather condition.
    temperature = weather_data['current']['temperature']  # Temperature in Fahrenheit.
    weather_conditions = weather_data['current']['weather_descriptions'][0]  # Current weather description.

    # HTML content using Bootstrap for styling.
    # Includes components like a responsive navbar, cards for displaying data, and a footer.
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>FITTZ: Weather Outfit Assistant</title>
        <!-- Bootstrap CSS for responsive design and modern styling -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet">
        <!-- Bootstrap Icons for adding icons to the page -->
        <link href="https://cdn.jsdelivr.net/npm/bootstrap-icons/font/bootstrap-icons.css" rel="stylesheet">
    </head>
    <body class="bg-light">
        <!-- Navbar: Displays the application name at the top of the page -->
        <nav class="navbar navbar-expand-lg navbar-light bg-light">
            <div class="container-fluid">
                <a class="navbar-brand text-success" href="#">FITTZ</a>
            </div>
        </nav>

        <!-- Main container for weather details and outfit recommendations -->
        <div class="container mt-5">
            <!-- Title Section -->
            <div class="text-center">
                <h1 class="display-4 text-success">FITTZ: Your Weather Outfit Assistant</h1>
                <h2 class="mt-4 text-muted">Weather Report for {city}</h2>
            </div>
            <!-- Weather Card: Displays temperature and weather condition -->
            <div class="card mt-4 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title"><i class="bi bi-thermometer-half"></i> Temperature: {temperature}°F</h5>
                    <p class="card-text"><i class="bi bi-cloud-sun"></i> Condition: {weather_conditions}</p>
                </div>
            </div>
            <!-- Recommendation Card: Displays the generated outfit recommendation -->
            <div class="card mt-4 shadow-sm">
                <div class="card-body">
                    <h5 class="card-title text-success"><i class="bi bi-emoji-smile"></i> Outfit Recommendation</h5>
                    <p class="card-text">{outfit_recommendation}</p>
                </div>
            </div>
        </div>

        <!-- Footer: Displays copyright information at the bottom of the page -->
        <footer class="text-center mt-5">
            <p class="text-muted">&copy; 2024 Fittz Weather Outfit Assistant</p>
        </footer>

        <!-- Bootstrap JS for interactive elements -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    # Write the generated HTML content to an output file.
    # This file can be opened in a browser to view the weather and outfit recommendation.
    with open("output.html", "w") as file:
        file.write(html_content)  # Save the HTML content to the file.