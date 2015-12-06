from collections import deque, OrderedDict
import json, re
from itertools import izip
import nltk
import miner

def clean(text):
	text = re.sub(r'<br />', ' ', text)
	text = re.sub(r'[^a-zA-Z\.]+', ' ', text)#remove anything thats not a letter
	return text.lower()

def read_and_tag(testfile):
    tok = nltk.word_tokenize(clean(testfile.read()))
    return nltk.pos_tag(tok)

pos = dict()
neg = dict()
found = dict()
queue = deque([])
id_num = 0

with open("found_pos_p.txt","r") as infile:
    pos = json.load(infile)

with open("found_pos.txt", "r") as infile:
    neg = json.load(infile)

with open("test.txt", "r") as testfile:
    t = read_and_tag(testfile)
    #match the text, get the interesting pos from this text
    for value in t:
        queue.append([value[0], value[1], miner.switcher(value[1])])
        if len(queue) > 3:
            queue.popleft()
        if len(queue) == 3:
            if miner.findPatterns(queue, found, id_num):
                id_num += 1

print("pos len:{0}",len(pos))
print("neg len:{0}",len(neg))

# for key, value in pos.items():
#     for n_key, n_value in neg.items():
#         if n_value == value:## - this doenst 100% work since we may delete one of the duplicate from neg we wont delete it again in pos
#             del neg[n_key]
#             del pos[key]
#             break

print("pos len:{0}",len(pos))
print("neg len:{0}",len(neg))

neg_count = 0
for key, value in found.iteritems():
    if value in neg.values():
        print(value)
        neg_count += 1

print (neg_count)

pos_count = 0
for key, value in found.iteritems():
    if value in pos.values():
        print(value)
        pos_count += 1

print (pos_count)
