import csv
import time
import json
import feedparser
import requests
import simplejson as json
from flask import Flask

start_time = time.clock()


#1 Open csv file and loop through data
inFile = open('news-sites.csv')
Reader = csv.reader(inFile)
Array1 = list(Reader)

for i in range (1, 329):
	a=Array1[i][2]
	
	#3 Download RSS content, parse with feedparser
	
	d=feedparser.parse(a)
	try:
		#try:
		x0 = d.feed.link
		#except AttributeError:
			#continue
		x1 = d.feed.image
		x2 = d.feed.title
		x3 = d.feed.description
		x4 = d.feed.date
		x5 = [x0,x1,x2,x3,x4]
	
		#4 Convert XML in RSS to JSON and output
		print(json.dumps(x5, sort_keys=True, indent=4 * ' '))
		#print(json.dumps(x1, sort_keys=True, indent=4 * ' '))
		#print(json.dumps(x2, sort_keys=True, indent=4 * ' '))
		#print(json.dumps(x3, sort_keys=True, indent=4 * ' '))
		#print(json.dumps(x4, sort_keys=True, indent=4 * ' '))
		
	except AttributeError:
		continue
	
	#Test
	#time.sleep(1)

#close file				
inFile.close()

print("=== %s seconds ---" % (time.clock() - start_time), 3)

#r=requests.get('http://www.wsj.com/xml/rss/3_7014.xml')
#print(r)
#print(r.json)
#print(r.status_code)
#print(r.headers)
#print(r.encoding)
#print(r.text)

#d=feedparser.parse('http://www.wsj.com/xml/rss/3_7014.xml')
#print(d)