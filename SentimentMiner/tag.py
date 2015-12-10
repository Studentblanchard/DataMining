## - Comp 4710 - Data Mining
## - Prof: Dr. Carson K. Leung
## - Authors: Trevor Blanchard, Stefan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

import datetime
from tagger import Tagger
from timer import Timer

myTagger = Tagger()
myTimer = Timer()

myTimer.start_timer()

print("\nFinding negative POS\n")

myTagger.tag("Train/neg/*.txt", "Train/neg_pos.txt")

print("\nFinding positive POS\n")

myTagger.tag("Train/pos/*.txt", "Train/pos_pos.txt")

myTimer.end_timer()
myTimer.summary()
