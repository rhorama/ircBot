import ircWeatherModule
import utils


def main(input):
    if len(input) == 0:
        return "error"
    inputList = input.split(" ")
    inputCommand = inputList[0]
    current_weather = ircWeatherModule.main(input.split(" ")[1], False)
    weather_forecast = ircWeatherModule.main(input.split(" ")[1], True)
    coin_flip = utils.flip()
    try:
        commandDict = {'!w': current_weather, '!wf': weather_forecast, '!cf': coin_flip}
        out = commandDict[inputCommand]
        return out
    except IndexError:
        return "not a valid command"