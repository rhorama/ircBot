class Logger:
    def __init__(self, logfile):
        self.logfile = logfile
    
    def info(self, message):
        file = open(self.logfile, "a")
        file.write(f"INFO: {message}")
        file.close()

    