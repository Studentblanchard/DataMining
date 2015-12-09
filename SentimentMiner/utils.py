## - Comp 4710 - Data Mining
## - Prof: Carson Leunig
## - Authors: Trevor Blanchard, Stepan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

import re, sys, json
from collections import OrderedDict

## - A set of utilites

def clean(text):
    text = re.sub(r'<.+/?>', ' ', text)# Remove html tags
    text = re.sub(r'[^a-zA-Z\.]+', ' ', text)# Remove anything thats not a letter
    return text.lower()

def update_display(amt, total):
    sys.stdout.write('\r')
    sys.stdout.write("[%-20s] %.2f%%" % ('='*(20*amt/total), 100*float(amt)/total))
    sys.stdout.flush()

def percentage(low, high):
    return int(100*(float(low)/high))

def load_json(filepath):
    with open(filepath,"r") as infile:
        return json.load(infile, object_pairs_hook=OrderedDict)

def dump_json(data,filepath):
    with open(filepath,"w") as outfile:
        json.dump(data, outfile, indent=4)
