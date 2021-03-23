import requests
import json
from utils import convertDate


def main(switchInput, f):
    apikey = "&appid=8e4c8e9d8b849b0a0d50b8797e5c6bea"
    currentWeatherUrl = "http://api.openweathermap.org/data/2.5/weather?q=" + \
        switchInput.strip(' ') + "&units=imperial" + apikey
    response = requests.get(currentWeatherUrl)

    json_data = response.json()

    try:
        weather = json_data["weather"]
    except TypeError:
        return "no weather data retrieved"
        
    mainWeather = json_data["main"]
    mainCondition = weather[0]["main"]
    conditionDesc = weather[0]["description"]
    temp = mainWeather["temp"]
    feelsLike = mainWeather["feels_like"]
    pressure = mainWeather["pressure"]
    humidity = mainWeather["humidity"]
    city = json_data["name"]
    country = json_data["sys"]["country"]
    wind = json_data["wind"]["speed"]
    lat = json_data["coord"]["lat"]
    lon = json_data["coord"]["lon"]
    coord = str(lat) + " | " + str(lon)
    out = [mainCondition, conditionDesc, temp, feelsLike,
           pressure, humidity, city, country, wind, coord]

    oneCallWeatherUrl = "https://api.openweathermap.org/data/2.5/onecall?lat=" + \
        str(lat) + "&lon=" + str(lon) + \
        "&exclude=minutely,hourly" + "&units=imperial" + apikey
    oneCallResponse = requests.get(oneCallWeatherUrl)
    oneCallJson = oneCallResponse.json()

    dailyString = "forecast: "
    daily = oneCallJson["daily"]
    for jsonDay in daily:
        udate = jsonDay["dt"]
        pdate = convertDate(udate)
        dailyString = dailyString + "|" + str(pdate)

    print(out)
    print(dailyString)
    if f == True:
        return dailyString
    else:
        return out
