## - Comp 4710 - Data Mining
## - Prof: Carson Leunig
## - Authors: Trevor Blanchard, Stefan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

from classifier import Classifier
from timer import Timer

myClassifier = Classifier()
myTimer = Timer()

myTimer.start_timer()
myClassifier.load()

folderpath = "Test/positivetestdata/*.txt"

myClassifier.classify_reviews(folderpath)

folderpath = "Test/negativetestdata/*.txt"

myClassifier.classify_reviews(folderpath)

myTimer.end_timer()
myTimer.summary()
