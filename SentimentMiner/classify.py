from classifier import Classifier
from timer import Timer

myClassifier = Classifier()
myTimer = Timer()

myTimer.start_timer()
myClassifier.load()

folderpath = "positivetestdata/*.txt"

myClassifier.classify_reviews(folderpath)

folderpath = "negativetestdata/*.txt"

myClassifier.classify_reviews(folderpath)

myTimer.end_timer()
myTimer.summary()
