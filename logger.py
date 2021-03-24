class Logger:
    def __init__(self, logfile):
        self.logfile = logfile
    
    def log_write(self, message):
        file = open(self.logfile, "a")
        file.write(str(message))
        file.close()

    