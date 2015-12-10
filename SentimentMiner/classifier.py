## - Comp 4710 - Data Mining
## - Prof: Dr. Carson K. Leung
## - Authors: Trevor Blanchard, Stefan Harris, Brett Small, Sam Peers
## - Sentiment Miner
## - December 10, 2015

import json, glob, re, utils

## - Classifies text based on our learned data
class Classifier:
	def __init__(self):
		self.pos_snip = []
		self.neg_snip = []

	## - Initalizes the positive and negative training data
	def load(self):
		pos = dict()
		neg = dict()
		with open("Train/positive_POS_dict.json","r") as infile:
			pos = json.load(infile)
		with open("Train/negative_POS_dict.json", "r") as infile:
			neg = json.load(infile)
		# make the tagged dictionary into a string
		for _, value in pos.iteritems():
			self.pos_snip.append((' '.join(item[0] for item in value)).strip())
        # Remove duplicates
		self.pos_snip = list(set(self.pos_snip))
		# make the tagged dictionary into a string
		for _, value in neg.iteritems():
			self.neg_snip.append((' '.join(item[0] for item in value)).strip())
        # Remove duplicates
		self.neg_snip = list(set(self.neg_snip))

	## - Takes a file (as text) and assigns a classfication
	def classify(self, testfile):
		text = utils.clean(testfile.read())
		neg_count = 0
		pos_count = 0
		for snip in self.neg_snip:
			if snip in text:
				neg_count += 1

		for snip in self.pos_snip:
			if snip in text:
				pos_count += 1

		return pos_count - neg_count

	## - Takes a directory path and classifies all the contained reviews
	def classify_reviews(self, folderpath):
		negc = 0
		posc = 0
		undc = 0
		total = 0
		filenames = glob.glob(folderpath)
		totalnumfiles = len(filenames)

		print("Testing data set")
		print("Number of files:{0}".format(totalnumfiles))

		if totalnumfiles == 0:
			print("No files to classify, exiting...")
			return

		for f in filenames:
			with open(f, 'r') as infile:
				clsfy = self.classify(infile)
				total += clsfy
				if clsfy > 0:
					posc += 1
				elif clsfy < 0:
					negc += 1
				elif clsfy == 0:
					undc += 1

		results = """
Results...
Average classification: {0}
Percentage of positve classifications: %{1}
Percentage of negative classifications: %{2}
Percentage of undertermined classifications: %{3}
		""".format(total/totalnumfiles,utils.percentage(posc, len(filenames)),utils.percentage(negc, len(filenames)),utils.percentage(undc, len(filenames)))
		print results

		utils.print_to_file("testResults.txt", "\nFolderpath: {0}\nNumber of Files: {1}\n{2}".format(folderpath,totalnumfiles,results))
