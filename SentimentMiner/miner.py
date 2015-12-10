## - Comp 4710 - Data Mining
## - Prof: Dr. Carson K. Leung
## - Authors: Trevor Blanchard, Stefan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

from collections import deque, OrderedDict
import re
from itertools import izip

## - regex representations of the POS tags
ADJECTIVE_RE = "^JJ(R|S)?$"
NOUN_RE = "^NN(P|S|PS)?$"
ADVERB_RE = "^RB(R|S)?$"
VERB_RE = "^VB(D|G|N|P|Z)?$"
OTHER_RE = "^.*$"

## - pos IDs
NOUN_ID = 1
VERB_ID = 2
ADJECTIVE_ID = 4
ADVERB_ID = 8
OTHER_ID = 16

## - queue entries for de-matchers
NOT_NN_RB_JJ = ["", "NN RB JJ", 0]
NOT_NN = ["", "NN", 0]
ANY = ["", "", 0]

## - combined IDs for interesting POS
JJ_NN = 5
RB_JJ = 12
JJ_JJ = 4
NN_JJ = 5
RB_VB = 10

## - Matches and mines interesting patterns from a given text
class Miner:
    def __init__(self):
        self.or_lambda = lambda q,p: p|q
        self.count_t = 0
        self.queue = deque([])
        self.found = dict()

    ## - Resets the miners internal variables
    def reset(self):
        self.count_t = 0
        self.found = dict()

    ## - Matches a part of speech and returns the ID
    def switcher(self, pos):
        if(re.match(ADJECTIVE_RE, pos)):
            return ADJECTIVE_ID
        if(re.match(NOUN_RE, pos)):
            return NOUN_ID
        if(re.match(VERB_RE, pos)):
            return VERB_ID
        if(re.match(ADVERB_RE, pos)):
            return ADVERB_ID
        if(re.match(OTHER_RE, pos)):
            return OTHER_ID

    ## - Replaces the starting list attribute
    def replace_start(self, pos_code):
        self.queue.popleft()
        self.queue.appendleft(pos_code)

    ## - Replaces the ending list attribute
    def replace_end(self, pos_code):
        self.queue.pop()
        self.queue.append(pos_code)

    ## - matches interesting patterns in parsed POS, return 1 when match found, else 0
    def findPatterns(self):
        matcher = reduce(self.or_lambda, [x[2] for x in self.queue])
        if matcher & JJ_NN:
            if (self.queue[0][2] & OTHER_ID or self.queue[0][2] & VERB_ID) and self.queue[1][2] & ADJECTIVE_ID and self.queue[2][2] & NOUN_ID:
                self.replace_start(NOT_NN_RB_JJ)
                self.found.update({self.count_t: list(self.queue)})
                return 1
            if self.queue[0][2] & NOUN_ID and self.queue[1][2] & ADJECTIVE_ID and not(self.queue[2][2] & NOUN_ID):
                self.replace_end(NOT_NN)
                self.found.update({self.count_t: list(self.queue)})
                return 1
        if matcher & RB_JJ:
            if self.queue[0][2] & ADVERB_ID and self.queue[1][2] & ADJECTIVE_ID and not(self.queue[2][2] & NOUN_ID):
                self.replace_end(NOT_NN)
                self.found.update({self.count_t: list(self.queue)})
                return 1
        if matcher & JJ_JJ:
            if self.queue[0][2] & ADVERB_ID and self.queue[1][2] & ADJECTIVE_ID and not(self.queue[2][2] & NOUN_ID):
                self.replace_end(NOT_NN)
                self.found.update({self.count_t: list(self.queue)})
                return 1
        if matcher & RB_VB:
            if self.queue[0][2] & ADVERB_ID and self.queue[1][2] & VERB_ID:
                self.replace_end(ANY)
                self.found.update({self.count_t: list(self.queue)})
                return 1
        return 0

    ## - Mines patterns in a give text
    def mine_text(self, full_text):
        self.queue = deque([])
        for key, word_pos in full_text.iteritems():
    		self.queue.append([key, word_pos, self.switcher(word_pos)])
    		if len(self.queue) > 3:
    			self.queue.popleft()
    		if len(self.queue) == 3:
    			self.count_t += self.findPatterns()
