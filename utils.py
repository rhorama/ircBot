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


def joinchan(chan, ircsock):
    ircsock.send(f"JOIN {chan}\n".encode())
    ircmsg = ""
    while ircmsg.find("End of /NAMES list.") == -1:
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        print(ircmsg)


def ping(ircsock):  # respond to server Pings.
    pong = "PONG"
    ircsock.send("PONG :pingis\n".encode())
    print(pong)


def sendmsg(ircsock, msg, target=channel):  # sends messages to the target.
    ircsock.send(f"PRIVMSG {target} :{msg}\n".encode())
