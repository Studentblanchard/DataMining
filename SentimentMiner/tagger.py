
import json, re, string, glob
from collections import Counter, OrderedDict
import nltk, sys, datetime, utils

## - Todo[add description]
class Tagger:
	def __init__(self):
		self.pos = dict()
		self.words = []
		self.total = 0

	## - Get the total number of reviews
	def get_total(self):
		self.total = 0
		for s in self.words:
			self.total += len(s)

	## - Loads and cleans the reviews into a list
	def load_words(self, folderpath):
		filenames = glob.glob(folderpath)
		limit = 0
		for f in filenames:
			with open(f, 'r') as infile:
				text = infile.read()
				text = utils.clean(text)
				self.words.append([text])
				limit += 1
				if limit == 20:
					break

	## - Tags the reviews at the specified directory
	def tag(self, folderpath, outpath):
		self.load_words(folderpath)
		self.get_total()
		key = 0
		for s in self.words:
			for k in s:
				text = nltk.word_tokenize(k)
				t = nltk.pos_tag(text)
				self.pos.update({key: OrderedDict(t)})
				key += 1
				utils.update_display(key, self.total)
		with open(outpath,"w") as out:
			json.dump(self.pos, out, indent=4)
