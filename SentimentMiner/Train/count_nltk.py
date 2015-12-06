
import json
import re
import string
import glob
from collections import Counter, OrderedDict
import nltk
import sys
import datetime

def clean(text):
	#text = re.sub(r'\'(?=[a-z]\b)', '', text)#remove apostrophes and replace them with emply space, ie don't becomes dont
	text = re.sub(r'<br />', ' ', text)
	text = re.sub(r'[^a-zA-Z\.]+', ' ', text)#remove anything thats not a letter

	return text.lower()

def get_num_sent(words):
	count = 0
	for s in words:
		count += len(s)
	return count

def count_words(folderpath, outpath):
	filenames = glob.glob(folderpath)
	words = []
	limit = 0
	for f in filenames:
		with open(f, 'r') as infile:
			text = infile.read()
			text = clean(text)
			words.append([text])
			limit += 1
			if limit == 20:
				break
	pos = dict()

	num_sent = get_num_sent(words)

	key = 0
	for s in words:
		for k in s:
			text = nltk.word_tokenize(k)
			t = nltk.pos_tag(text)
			pos.update({key: OrderedDict(t)})
			key += 1
			sys.stdout.write('\r')
			sys.stdout.write("[%-20s] %.2f%%" % ('='*(20*key/num_sent), 100*float(key)/num_sent))
			sys.stdout.flush()
	with open(outpath,"w") as out:
		json.dump(pos,out,indent=4)
	print("\n")

start = datetime.datetime.now()
print("Starting at: {0}".format(start.time()))

print("Finding negative POS\n")
count_words("Data/aclImdb/train/neg/*.txt", "neg_pos.txt")
print("Finding positive POS\n")
count_words("Data/aclImdb/train/pos/*.txt", "pos_pos.txt")

end = datetime.datetime.now()
print("Finished at: {0}".format(end.time()))

print("Total time: {0}".format((end-start).total_seconds()))
