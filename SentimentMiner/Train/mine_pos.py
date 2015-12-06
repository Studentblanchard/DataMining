from collections import deque, OrderedDict
import json, re
from itertools import izip
import miner

## - regex representations of the POS tags
ADJECTIVE_RE = "^JJ(R|S)?$"
NOUN_RE = "^NN(P|S|PS)?$"
ADVERB_RE = "^RB(R|S)?$"
VERB_RE = "^VB(D|G|N|P|Z)?$"
OTHER_RE = "^.*$"

NOUN_ID = 1
VERB_ID = 2
ADJECTIVE_ID = 4
ADVERB_ID = 8
OTHER_ID = 16

NOT_NN_RB_JJ = ["", "NN RB JJ", 0]
NOT_NN = ["", "NN", 0]
ANY = ["", "", 0]

JJ_NN = 5
RB_JJ = 12
JJ_JJ = 4
NN_JJ = 5
RB_VB = 10

data = OrderedDict()
found = dict()


with open("pos_pos.txt","r") as infile:
    data = json.load(infile, object_pairs_hook=OrderedDict)

def switcher(pos):
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

queue = deque([])

or_lambda = lambda q,p: p|q
matcher = 0
count_t = 0
print(len(data))
for k, v in data.iteritems():
    for key, value in v.iteritems():
        queue.append([key, value, switcher(value)])
        if len(queue) > 3:
            queue.popleft()
        if len(queue) == 3:
            matcher = reduce(or_lambda, [x[2] for x in queue])
            count_t += findPatterns(queue, matcher, found)

with open("found_pos_p.txt","w") as outfile:
    json.dump(found, outfile, indent=4)
