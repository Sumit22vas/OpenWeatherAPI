import requests
import os
from dotenv import load_dotenv
# load environment variables
load_dotenv()

def get_current_weather():
    
    # collect user input for city
    city = input("\n\n Enter City Name : \n\n")

    req_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={os.getenv("OW_API_KEY")}&units=metric"

    weather_data = requests.get(req_url).json()
    
    if weather_data["cod"] == 200:
        print(f"Weather Update : Today in {weather_data["name"]}")
        print(f"Current Temperature : {weather_data["main"]["temp"]}")
        print(f"Humidity : {weather_data["main"]["humidity"]}")
        print(f"Today's Minimum Temp : {weather_data["main"]["temp_min"]}")
        print(f"Today's Maximum Temp : {weather_data["main"]["temp_max"]}")
        print(f"Description : {weather_data["weather"][0]["description"]}, Feels like {weather_data["main"]["feels_like"]}")
    else:
        print("Something went wrong")
        return get_current_weather()


