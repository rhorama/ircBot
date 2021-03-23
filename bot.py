import socket
import time
import switchboard
import utils
import core

server = "irc.irchighway.net"
channel = "#fart"
botnick = "rhobot"
adminname = "rhorama"
class Bot:
    def __init__(self, server, channel, botnick, adminname):
        self.server = server
        self.channel = channel
        self.botnick = botnick
        self.adminname = adminname
        
        

    def run(self):
        ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ircsock.connect((server, 6660))
        ircsock.send(f"USER {botnick} {botnick} {botnick} {botnick}\n".encode())
        ircsock.send(f"NICK {botnick}\n".encode())
        time.sleep(2)
        utils.joinchan(channel, ircsock)
        core.main(ircsock)

bot1 = Bot(server, channel, botnick, adminname)
bot1.run()