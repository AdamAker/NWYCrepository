import json
import feedparser

def OutputAppend(A4):

	#create output dictionary
	output=[]

	#loop over all rows in A4 and access column 2: the location of the rss feed
	for row in A4:
		a=row[2]
	
		#3 Download RSS content, parse with feedparser
		if a == '0':
			#print(a)
			continue
			
		elif a != '0':
			#print(a)
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
				#output.append({'you done goofed'})
				continue
	
	return output
	