import datetime

class Timer:
    def __init__(self):
        self.start = 0
        self.end = 0

    def start_timer(self):
        self.start = datetime.datetime.now()
        print("Starting at: {0}".format(self.start.time()))

    def end_timer(self):
        self.end = datetime.datetime.now()
        print("Finished at: {0}".format(self.end.time()))

    def summary(self):
        print("Total time: {0}".format((self.end-self.start).total_seconds()))
