import weather_module
from utils import flip


def main(input):
    if len(input) == 0:
        return "error"
    input_items = input.split(" ")
    input_command = input_items[0]
    input_args = input_items[1:]
    try:
        command_data = {'!w': weather_module.main, '!cf': flip}
        out = command_data[input_command]
        if len(input_args) == 0:
            try:
                return out()
            except TypeError as te:
                return f"TypeError: {te}"
        try:
            return out(input_args)
        except TypeError as te:
            return f"TypeError: {te}"
    except IndexError as ie:
        return f"IndexError: Not a valid command. Exception info: {ie}"