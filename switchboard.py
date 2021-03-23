import ircWeatherModule
import utils


def main(input):
    if len(input) == 0:
        return "error"
    inputList = input.split(" ")
    inputCommand = inputList[0]
    try:
        commandDict = {'!w': ircWeatherModule.main(input.split(" ")[1], True), '!wf': ircWeatherModule.main(input.split(" ")[1], True), '!cf': utils.flip()}
        out = commandDict[inputCommand]
        return out
    except IndexError:
        return "not a valid command"