import socket
import time
import switchboard
import utils
import core

server = "irc.irchighway.net"
channel = "#fart"
botnick = "rhobot"
adminname = "rhorama"
port = 6660
class Bot:
    def __init__(self, server, channel, botnick, adminname):
        self.server = server
        self.channel = channel
        self.botnick = botnick
        self.adminname = adminname
        
    def create_socket(self, server_address, server_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((server_address, server_port))
        return sock

    def run(self):
        ircsock = self.create_socket(server, port)
        ircsock.send(f"USER {botnick} {botnick} {botnick} {botnick}\n".encode())
        ircsock.send(f"NICK {botnick}\n".encode())
        time.sleep(2)
        utils.joinchan(channel, ircsock)
        core.main(ircsock)

bot1 = Bot(server, channel, botnick, adminname)
bot1.run()