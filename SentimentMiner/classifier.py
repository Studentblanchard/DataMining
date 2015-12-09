import json, glob, re, utils

class Classifier:
	def __init__(self):
		self.pos_snip = []
		self.neg_snip = []

	## - Initalizes the positive and negative training data
	def load(self):
		pos = dict()
		neg = dict()
		with open("positive_POS.txt","r") as infile:
			pos = json.load(infile)
		with open("negative_POS.txt", "r") as infile:
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
		filenames = glob.glob(folderpath)
		print("Testing data set")
		print("Number of files:{0}".format(len(filenames)))
		for f in filenames:
			with open(f, 'r') as infile:
				clsfy = self.classify(infile)
				if clsfy > 0:
					posc += 1
				if clsfy < 0:
					negc += 1
				if clsfy == 0:
					undc += 1

		print("Results...")
		print("Percentage of positve classifications: %{0}".format(utils.percentage(posc, len(filenames))))
		print("Percentage of negative classifications: %{0}".format(utils.percentage(negc, len(filenames))))
		print("Percentage of undertermined classifications: %{0}".format(utils.percentage(undc, len(filenames))))
