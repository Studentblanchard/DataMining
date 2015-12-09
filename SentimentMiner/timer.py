## - Comp 4710 - Data Mining
## - Prof: Carson Leunig
## - Authors: Trevor Blanchard, Stepan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

import datetime

## - A timer utility
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
