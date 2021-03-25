import socket
import time
import switchboard
import utils
import logger

# these vars will live in a config file eventually
server = "irc.irchighway.net"
channel = "#fart"
botnick = "rhobot"
adminname = "rhorama"
port = 6660
logfile = "test.txt"


class Bot:

    def __init__(self, server, port, channel, botnick, adminname, logger):
        self.server = server
        self.port = port
        self.channel = channel
        self.botnick = botnick
        self.adminname = adminname
        self.logger = utils.get_logger()
        self.ircsock = self.create_socket()

    def joinchan(self, chan):
        self.ircsock.send(f"JOIN {chan}\n".encode())
        ircmsg = ""
        while ircmsg.find("End of /NAMES list.") == -1:
            ircmsg = self.ircsock.recv(2048).decode("UTF-8")
            ircmsg = ircmsg.strip('\n\r')
            print(ircmsg)

    # respond to server Pings
    def ping(self):
        pong = "PONG"
        self.ircsock.send("PONG :pingis\n".encode())
        print(pong)

    # sends messages to the target.
    def sendmsg(self, msg, target=channel):
        self.ircsock.send(f"PRIVMSG {target} :{msg}\n".encode())

    def create_socket(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server, self.port))
        return sock

    def run(self):
        self.ircsock.send(
            f"USER {botnick} {botnick} {botnick} {botnick}\n".encode())
        self.ircsock.send(f"NICK {botnick}\n".encode())
        time.sleep(2)
        self.joinchan(channel)
        self.listener()

    def listener(self):
        while 1:
            exitcode = f"bye  + {botnick}"
            ircmsg = self.ircsock.recv(2048).decode("UTF-8")
            ircmsg = ircmsg.strip('\n\r')
            if ircmsg.find("PING :") != -1:
                self.ping()
            if ircmsg.find("PRIVMSG") != -1:
                name = ircmsg.split('!', 1)[0][1:]
                message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
                if len(name) < 17:
                    if message.startswith("!"):
                        mes = str(switchboard.main(
                            message.rstrip()))
                        if mes != "error" and mes != -1:
                            self.sendmsg(mes)
                    if message[:5].find('.tell') != -1:
                        target = message.split(' ', 1)[1]
                        if target.find(' ') != -1:
                            message = target.split(' ', 1)[1]
                            target = target.split(' ')[0]
                        else:
                            target = name
                            message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
                            self.sendmsg(message, target)
                if name.lower() == adminname.lower():
                    if message.rstrip() == exitcode:
                        print("exit code received")
                        self.ircsock.send("QUIT \n".encode())
                        return

#eventually need to move startup to own files
bot1 = Bot(server, port, channel, botnick, adminname, logfile)
bot1.run()
