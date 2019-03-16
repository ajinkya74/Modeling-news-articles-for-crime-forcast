# -*- coding: utf-8 -*-

import json
#import simplejson  # simplejson provides more descriptive error message
import os
#import datefinder
from HTMLParser import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

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
print 'Running...'
for filename in os.listdir(os.getcwd()):
	if ((filename != 'countryfinder.py') and (filename != 'countryfiles') and (filename != 'filefinder.py')):   #('dir' not in filename):		
		with open(filename) as f:
			for line in f:
				line = line.strip()
				if line:
					jsonData = line
					try:
						toPython = json.loads(jsonData)
						for key, value in toPython.items():
							if key == 'embersGeoCode':
								country = value.get('country')
								if country != '' and country != '-':
									if not os.path.exists('countryfiles/' + country):
										newdir = 'countryfiles/' + country
										os.makedirs(newdir)
										fname = newdir + '/' + filename 
										if os.path.isfile(fname):
											ff = open(fname, 'a+')
											ff.write(line)
											ff.write('\n')
											ff.close()
										else:
											ff = open(fname, 'a+')
											ff.write(line)
											ff.write('\n')
											ff.close()
									else:
										fname = 'countryfiles/' + country + '/' + filename 
										if os.path.isfile(fname):
											ff = open(fname, 'a+')
											ff.write(line)
											ff.write('\n')
											ff.close()
										else:
											ff = open(fname, 'a+')
											ff.write(line)
											ff.write('\n')
											ff.close()
								else:
									fname = 'countryfiles/' +  'nocountry/' + filename 
									if os.path.isfile(fname):
										ff2 = open(fname, 'a+')
										ff2.write(line)
										ff2.write('\n')
										ff2.close()
									else:
										ff2 = open(fname, 'a+')
										ff2.write(line)
										ff2.write('\n')
										ff2.close()
					except ValueError as e:
						print (e, fname)
						pass
								
				
					