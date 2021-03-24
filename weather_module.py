import requests
import json
import os
from dotenv import load_dotenv
from utils import convert_date


def main(switch_input, f):
    load_dotenv()
    apikey = os.getenv('APIKEY_OPENWEATHERMAP')
    current_weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={switch_input.strip(' ')}&units=imperial&appid={apikey}"
    response = requests.get(current_weather_url)
    weather_table = {}

    json_data = response.json()

    try:
        weather = json_data["weather"]
    except TypeError:
        print(f"typeError Exception: cannot find weather data in {weather}")
        return "TypeError Exception: Cannot find weather data"

    
    main_weather = json_data["main"]
    weather_table['main condition'] = weather[0]["main"]
    weather_table['condition description'] = weather[0]["description"]
    weather_table['temp'] = main_weather["temp"]
    weather_table['feels like'] = main_weather["feels_like"]
    weather_table['pressure'] = main_weather["pressure"]
    weather_table['humidity'] = main_weather["humidity"]
    weather_table['city'] = json_data["name"]
    weather_table['country'] = json_data["sys"]["country"]
    weather_table['wind'] = json_data["wind"]["speed"]
    weather_table['latitude'] = json_data["coord"]["lat"]
    weather_table['longitude'] = json_data["coord"]["lon"]
    weather_table['coord'] = f"{weather_table['lat']}|{weather_table['lon']}"
    out = []
    for item in weather_table:
        out.append(f"{item}: {weather_table[item]}")

    one_call_weather_url = f"https://api.openweathermap.org/data/2.5/onecall?lat={weather_table['lat']}&lon={weather_table['lon']}&exclude=minutely,hourly&units=imperial&appid={apikey}"
    one_call_response = requests.get(one_call_weather_url)
    one_call_json = one_call_response.json()

    daily_weather_string = "forecast: "

    try:
        daily = one_call_json["daily"]
        for json_day in daily:
            unix_date = json_day["dt"]
            readable_date = convert_date(unix_date)
            daily_weather_string = f"{daily_weather_string}|{readable_date}"
    except KeyError:
        return "Key Exception: Can't find key Daily"
    if f == True:
        print(daily_weather_string)
        return daily_weather_string
    else:
        print(out)
        return out
