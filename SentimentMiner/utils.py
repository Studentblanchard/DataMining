import re, sys

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
