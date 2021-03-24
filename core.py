import socket
import utils
import switchboard


def main(ircsock):
    while 1:
        botnick = "rhobot"
        adminname = "rhorama"
        exitcode = f"bye  + {botnick}"
        ircmsg = ircsock.recv(2048).decode("UTF-8")
        ircmsg = ircmsg.strip('\n\r')
        if ircmsg.find("PING :") != -1:
            utils.ping(ircsock)
        if ircmsg.find("PRIVMSG") != -1:
            name = ircmsg.split('!', 1)[0][1:]
            message = ircmsg.split('PRIVMSG', 1)[1].split(':', 1)[1]
            if len(name) < 17:
                if message.startswith("!"):
                    mes = str(switchboard.main(
                        message.rstrip()))
                    if mes != "error" and mes != -1:
                        utils.sendmsg(ircsock, mes)
                if message[:5].find('.tell') != -1:
                    target = message.split(' ', 1)[1]
                    if target.find(' ') != -1:
                        message = target.split(' ', 1)[1]
                        target = target.split(' ')[0]
                    else:
                        target = name
                        message = "Could not parse. The message should be in the format of ‘.tell [target] [message]’ to work properly."
                        utils.sendmsg(ircsock, message, target)
            if name.lower() == adminname.lower():
                if message.rstrip() == exitcode:
                    print("exit code received")
                    ircsock.send("QUIT \n".encode())
                    return
               # if message.rstrip() == "resetBot":
               #     reloadAll()

