import random
import datetime
import socket

channel = "##fart-bot-test"

def flip():
    if random.randint(0,1) == 1:
        return "Heads"
    else:
        return "Tails"

def convertDate(unixDate):
    out = datetime.datetime.fromtimestamp(int(unixDate)).strftime('%m-%d')
    return out

def joinchan(chan, ircsock):
    ircsock.send(bytes("JOIN " + chan + '\n', "UTF-8"))
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
    ircsock.send(bytes("PRIVMSG " + target + " :" + msg + '\n', "UTF-8"))

