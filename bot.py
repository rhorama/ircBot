import socket
import time
import switchboard
import utils
import core

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server = "irc.irchighway.net"
channel = "#fart"
botnick = "rhobot"
adminname = "rhorama"



ircsock.connect((server, 6660))
ircsock.send(f"USER {botnick} {botnick} {botnick} {botnick}\n".encode())
ircsock.send(f"NICK {botnick}\n".encode())
time.sleep(2)
utils.joinchan(channel, ircsock)


def main():
    core.main(ircsock)


main()
