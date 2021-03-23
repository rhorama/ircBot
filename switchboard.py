import ircWeatherModule
import utils


def main(input):
    commandList = ["!w", "!wf", "!cf"]
    if len(input) == 0:
        return "error"
    for command in commandList:
        if command in input:
            if command == commandList[0]:
                return ircWeatherModule.main(input.split(" ")[1], False)
            elif command == commandList[1]:
                return ircWeatherModule.main(input.split(" ")[1], True)
            else:
                return utils.flip()
    return "no command"