import weather_module
import utils


def main(input):
    if len(input) == 0:
        return "error"
    input_items = input.split(" ")
    input_command = input_items[0]
    input_args = input_items[1:]
    try:
        command_data = {'!w': weather_module.main, '!cf': utils.flip}
        out = command_data[input_command]
        return out(input_args)
    except IndexError:
        return "not a valid command"