import weather_module
import utils


def main(input):
    if len(input) == 0:
        return "error"
    input_items = input.split(" ")
    input_command = input_items[0]
    current_weather = weather_module.main(input.split(" ")[1], False)
    weather_forecast = weather_module.main(input.split(" ")[1], True)
    coin_flip = utils.flip()
    try:
        command_data = {'!w': current_weather, '!wf': weather_forecast, '!cf': coin_flip}
        out = command_data[input_command]
        return out
    except IndexError:
        return "not a valid command"