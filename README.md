Weather-Based Outfit Assistant

Justis Geronimo Peppin

I often struggle with choosing the right outfit when preparing to head out. Here in Seattle, I have experienced
many unpredictable weather conditions. I could check the weather for the day manually by myself, but those
weather conditions do not translate to what I should wear. The project I am taking on, Weather-Based Outfit
Assistant, aims to solve my problem by providing outfit suggestions based on the weather for the day. My
intended audience includes those needing quick and simple recommendations for their clothing based on their
weather conditions. I believe it will be beneficial for people who live in areas with unpredictable weather
conditions or those who frequently travel around the globe. I want my user to have a perfect outfit for their
day’s weather without even needing to look outside.


APIs/Modules

To implement this project idea, I want to use the WeatherStack API to get the weather data based on the city the
user inputs. This data will contain the temperature, weather conditions (sun, rain snow, etc.) and the wind speed.
The program will suggest clothing choices to the user their location. I will use the Requests Python Library to
retrieve and then process this data from the API, this should help access the API smoothly. I also want to
challenge myself by trying to use the ipinfo.io API to obtain the users geolocation based on their IP address
without the need for user input.


Output

The intended output format will be a HTML webpage that will display the weather information and outfit
recommendations in an easy-to-understand way (hopefully visually appealing).

The webpage should include the following:
- Weather information:
o The current temperature, the weather description, and the user’s city name.
- The outfit suggestions:
o The clothing recommendations based on the weather data, say for example, jackets and hoodies
for colder days or umbrellas and raincoats for a rainy day.

The HTML formatting will allow the user to see the information in their web browser so that it is accessible and
user friendly.


Stretch Goals

If the project schedule is consistent and the functionality of the webpage is as intended, I have a couple of
“stretch goals” that could increase the usefulness and scope of the project:

- Hourly weather forecast for the day
o This feature would offer recommendations that will account for weather changes throughout the
day. For an example, the user could be reminded to bring an umbrella if it is expected to rain.
This functionality would help users plan their attire to stay comfortable as conditions change.

- UV index for sun protection
o Including the UV index along with the forecast would provide users with a reminder to bring sun
protection when the UV is high. It would require integrating an additional API that would
provide the data. This is a stretch goal because it involves setting up a second API and ensuring
compatibility with the Weatherstack data.

- Additional accessories
o The feature would expand those recommendations to include common accessories such as warm
hats, sunglasses, gloves, socks, thermal layers (if really needed). The feature could suggest
specific items based on the weather to keep the user comfortable. For example, gloves are
recommended if temperatures are very cold, or sunglasses if it is a bright and sunny day.


Development Plan

Week 1 - Set up accounts with Weatherstack and ipinfo.io to obtain API keys.
- Write a Python script to access user location via IP and fetch weather data for the
detected city.
- Display basic weather data in the console to confirm API functionality.
- 
Week 2 - Develop logic for outfit recommendations based on temperature and weather
descriptions.
- Create an HTML template to display the weather data and outfit suggestions in a user-
friendly format.
- Test the HTML output to ensure data displays correctly in various browsers.
  
Week 3 - Refine the HTML and CSS styling for a more polished look.
- Add optional features (see above) if there is time, beginning with the highest priority
stretch goals.
- Finalize the project and prepare for the presentation.
