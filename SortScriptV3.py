import csv
import json
import feedparser


#1 Open csv file and loop through data
inFile = open('news-sites.csv')
Reader = csv.reader(inFile)
Array1 = list(Reader)
output=[]

for row in Array1:
	a=row[2]
	
		#3 Download RSS content, parse with feedparser
	
	d=feedparser.parse(a)
	try:
		
		x0 = d.feed.link
		x1 = d.feed.image
		x2 = d.feed.title
		x3 = d.feed.description
		x4 = d.feed.date
		
		output.append({
		'link': d.feed.link,
		'image': d.feed.image,
		'title': d.feed.title,
		'description': d.feed.description,
		'date': d.feed.date
		})
			
	except AttributeError:
		
		continue
		
#4 Convert XML in RSS to JSON and output

print(json.dumps(output, sort_keys=True, indent=4 * ' '))

#close file				
inFile.close()
