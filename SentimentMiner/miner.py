## - Sentiment Miner

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



class Miner:
    def __init__(self):
        self.or_lambda = lambda q,p: p|q

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
    def replace_start(self, queue, pos_code):
        queue.popleft()
        queue.appendleft(pos_code)

    ## - Replaces the ending list attribute
    def replace_end(self, queue, pos_code):
        queue.pop()
        queue.append(pos_code)

    ## - matches interesting patterns in parsed POS, return 1 when match found, else 0
    def findPatterns(self, queue, found, id_num):
        matcher = reduce(self.or_lambda, [x[2] for x in queue])
        if matcher & JJ_NN:
            if (queue[0][2] & OTHER_ID or queue[0][2] & VERB_ID) and queue[1][2] & ADJECTIVE_ID and queue[2][2] & NOUN_ID:
                self.replace_start(queue, NOT_NN_RB_JJ)
                found.update({id_num: list(queue)})
                return 1
            if queue[0][2] & NOUN_ID and queue[1][2] & ADJECTIVE_ID and not(queue[2][2] & NOUN_ID):
                self.replace_end(queue, NOT_NN)
                found.update({id_num: list(queue)})
                return 1
        if matcher & RB_JJ:
            if queue[0][2] & ADVERB_ID and queue[1][2] & ADJECTIVE_ID and not(queue[2][2] & NOUN_ID):
                self.replace_end(queue, NOT_NN)
                found.update({id_num: list(queue)})
                return 1
        if matcher & JJ_JJ:
            if queue[0][2] & ADVERB_ID and queue[1][2] & ADJECTIVE_ID and not(queue[2][2] & NOUN_ID):
                self.replace_end(queue, NOT_NN)
                found.update({id_num: list(queue)})
                return 1
        if matcher & RB_VB:
            if queue[0][2] & ADVERB_ID and queue[1][2] & VERB_ID:
                self.replace_end(queue, ANY)
                found.update({id_num: list(queue)})
                return 1
        return 0
