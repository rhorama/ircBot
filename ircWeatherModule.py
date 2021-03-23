import requests
import json
import os
from dotenv import load_dotenv
from utils import convertDate


def main(switchInput, f):
    load_dotenv()
    apikey = os.getenv('APIKEY_OPENWEATHERMAP')
    currentWeatherUrl = f"http://api.openweathermap.org/data/2.5/weather?q={switchInput.strip(' ')}&units=imperial&appid={apikey}"
    response = requests.get(currentWeatherUrl)
    weatherDict = {}

    json_data = response.json()

    try:
        weather = json_data["weather"]
    except TypeError:
        return "no weather data retrieved"

    
    mainWeather = json_data["main"]
    weatherDict['mainCondition'] = weather[0]["main"]
    weatherDict['conditionDesc'] = weather[0]["description"]
    weatherDict['temp'] = mainWeather["temp"]
    weatherDict['feelsLike'] = mainWeather["feels_like"]
    weatherDict['pressure'] = mainWeather["pressure"]
    weatherDict['humidity'] = mainWeather["humidity"]
    weatherDict['city'] = json_data["name"]
    weatherDict['country'] = json_data["sys"]["country"]
    weatherDict['wind'] = json_data["wind"]["speed"]
    weatherDict['lat'] = json_data["coord"]["lat"]
    weatherDict['lon'] = json_data["coord"]["lon"]
    weatherDict['coord'] = f"{weatherDict['lat']} +  |  {weatherDict['lon']}"
    out = []
    for item in weatherDict:
        out.append(item)

    oneCallWeatherUrl = "https://api.openweathermap.org/data/2.5/onecall?lat=" + \
        str(weatherDict['lat']) + "&lon=" + str(weatherDict['lon']) + \
        "&exclude=minutely,hourly" + "&units=imperial" + apikey
    oneCallResponse = requests.get(oneCallWeatherUrl)
    oneCallJson = oneCallResponse.json()

    dailyString = "forecast: "

    try:
        daily = oneCallJson["daily"]
        for jsonDay in daily:
            udate = jsonDay["dt"]
            pdate = convertDate(udate)
            dailyString = dailyString + "|" + str(pdate)
    except KeyError:
        return "key error"
    print(out)
    print(dailyString)
    if f == True:
        return dailyString
    else:
        return out
