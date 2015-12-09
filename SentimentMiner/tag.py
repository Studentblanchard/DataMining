import datetime
from tagger import Tagger
from timer import Timer

myTagger = Tagger()
myTimer = Timer()

myTimer.start_timer()

print("\nFinding negative POS\n")
myTagger.tag("Data/aclImdb/train/neg/*.txt", "neg_pos.txt")

print("\nFinding positive POS\n")
myTagger.tag("Data/aclImdb/train/pos/*.txt", "pos_pos.txt")

myTimer.end_timer()
myTimer.summary()
