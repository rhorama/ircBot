import socket
import time
import switchboard
import utils
import core

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.irchighway.net"
channel = "##fart-bot-test"
botnick = "rhobot"
adminname = "rhorama"

ircsock.connect((server, 6660))
ircsock.send(bytes("USER " + botnick + " " + botnick +
             " " + botnick + " " + botnick + '\n', "UTF-8"))
ircsock.send(bytes("NICK " + botnick + '\n', "UTF-8"))
time.sleep(2)
utils.joinchan(channel, ircsock)

def main():
    core.main(ircsock)
main()