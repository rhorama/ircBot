import random
import datetime
import socket

channel = "#fart"


def flip():
    if random.randint(0, 1) == 1:
        return "Heads"
    else:
        return "Tails"


def convert_date(unixDate):
    out = datetime.datetime.fromtimestamp(int(unixDate)).strftime('%m-%d')
    return out




