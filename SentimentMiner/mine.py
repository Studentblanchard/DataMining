## - Comp 4710 - Data Mining
## - Prof: Dr. Carson K. Leung
## - Authors: Trevor Blanchard, Stafan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

from miner import Miner
import utils
from timer import Timer

myTimer = Timer()
myMiner = Miner()

myTimer.start_timer()

print "\nMining for negative patterns\n"

data = utils.load_json("Train/neg_pos.txt")

for index, full_text  in data.iteritems():
	myMiner.mine_text(full_text)

utils.dump_json(myMiner.found,"Train/negative_POS_dict.json")

print "\nDone mining for negative patterns\n"

myMiner.reset()

print "\nMining for positive patterns\n"

data = utils.load_json("Train/pos_pos.txt")

for index, full_text  in data.iteritems():
	myMiner.mine_text(full_text)

utils.dump_json(myMiner.found,"Train/positive_POS_dict.json")

print "\nDone mining for positive patterns\n"

myTimer.end_timer()
myTimer.summary()
