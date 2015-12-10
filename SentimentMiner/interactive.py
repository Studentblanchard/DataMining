## - Comp 4710 - Data Mining
## - Prof: Carson Leunig
## - Authors: Trevor Blanchard, Stefan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

## - An interactive classifier

import sys
from classifier import Classifier

print "\nPlease wait while the training data is loaded.."

myClassifier = Classifier()
myClassifier.load()

print "Ready for input"

filename = raw_input("Enter a file name or a directory (type \"quit\" to quit) > ")

while filename != "quit":
    if ".txt" in filename:
        with open(filename, 'r') as infile:
            clsfy = myClassifier.classify(infile)
            if clsfy > 0:
                print "Positive! Weight = {0}".format(clsfy)
            elif clsfy < 0:
                print "Negative! Weight = {0}".format(clsfy)
            elif clsfy == 0:
                print "Undertermined"
    else:
        myClassifier.classify_reviews(filename + "*.txt")

    filename = raw_input("Enter a file name or a directory > ")
