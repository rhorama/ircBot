import random
import datetime
import socket
from logger import Logger

channel = "#fart"


def flip():
    if random.randint(0, 1) == 1:
        return "Heads"
    else:
        return "Tails"


def convert_date(unixDate):
    out = datetime.datetime.fromtimestamp(int(unixDate)).strftime('%m-%d')
    return out

def get_logger():
    logg = Logger("testlog.txt")
    return logg