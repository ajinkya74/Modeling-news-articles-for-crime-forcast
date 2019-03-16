# -*- coding: utf-8 -*-

# find homicide files

import json
#import simplejson  # simplejson provides more descriptive error message
import os
from HTMLParser import HTMLParser
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import PorterStemmer
from nltk.stem import SnowballStemmer


stemmer = SnowballStemmer("spanish")

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

i = 1
count = 0
found = 0
found2 = 0
date = ""
match = ""
print 'Running.'
#print 'changed'

for filename in os.listdir(os.getcwd()):
	i = 1
	if ((filename != 'cityfinder2.py') and  (filename != 'bogota') and (filename != 'cali') and (filename != 'medellin')and (filename != 'cartagena')):   #('dir' not in filename):		
		with open(filename) as f:
			fname1 = 'bogota/' + filename	
			fname2 = 'cali/' + filename
			fname3 = 'medellin/' + filename
			fname4 = 'cartagena/' + filename
			ff1 = open(fname1, 'a+')
			ff2 = open(fname2, 'a+')
			ff3 = open(fname3, 'a+')
			ff4 = open(fname4, 'a+')
			ff1.truncate()
			ff2.truncate()
			ff3.truncate()
			ff4.truncate()
			for line in f:
				line = line.strip()
				if line:
					foundb = 0
					foundc = 0
					foundm = 0
					tokens2 = []
					tokens4 = []
					lemmas1 = []
					jsonData = line
					try:
						toPython = json.loads(jsonData)
						for key, value in toPython.items():
							if key == 'content_title':
								string = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
								plain_string = strip_tags(string)
								tokenizer = RegexpTokenizer(r'\w+')
								raw = plain_string.lower()
								tokens = tokenizer.tokenize(raw)
								tokens2 = [x.lower() for x in tokens if x is not None]
							if key == 'Content' or key == 'content':
								string1 = value.lstrip('\n').rstrip('\n').replace('\n', ' ')
								plain_string1 = strip_tags(string1)
								tokenizer = RegexpTokenizer(r'\w+')
								raw1 = plain_string1.lower()
								tokens3 = tokenizer.tokenize(raw1)
								tokens4 = [x.lower() for x in tokens3 if x is not None]
							if key == 'BasisEnrichment':
								lemmas = []
								tokens = value.get('tokens')		
								found = 0
								for i in range(len(tokens)):	
									item = tokens[i]				
									for key in item:				
										if key == 'lemma':
											lemmas.append(item[key])
								lemmas1 = [l.lower() for l in lemmas if l is not None]
					except ValueError as e:
						print e
						#print (e, fname)
						pass
					bg = (unicode('BOGOTÁ', 'utf-8'))
					if (('bogota' in tokens2) or ('bogota' in tokens4) or ('bogota' in lemmas1) or (bg.lower() in tokens2) or (bg.lower() in tokens4) or (bg.lower() in lemmas1)):
						foundb = 1
						ff1.write(line)
						ff1.write('\n')
					if ('cali' in tokens2) or ('cali' in tokens4) or ('cali' in lemmas1):
						foundc = 1
						ff2.write(line)
						ff3.write('\n')
					if ('medellin' in tokens2) or ('medellin' in tokens4) or ('medellin' in lemmas1):
						foundm = 1
						ff3.write(line)
						ff3.write('\n')
					if ('cartagena' in tokens2) or ('cartagena' in tokens4) or ('cartagena' in lemmas1):
						foundm = 1
						ff4.write(line)
						ff4.write('\n')
			ff1.close()
			ff2.close()
			ff3.close()
			ff4.close()
				