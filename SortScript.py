import csv
import time
import json
import feedparser
import requests
from flask import Flask

#Code to skip the first line because "readerobj.line_num ==1"
	#csvRows[]
	#csvFileObj = open('news-sites.csv')
	#readerobj = csv.reader(csvFileObj)
	#for row in readerobj:
	#	if readerobj.line_num ==1:
	#		continue 
	#	csvRows.append(row)
	#csvFileObj.close()

#Setting up Reading and Writing csv files.

#csvRows = []
inFile = open('news-sites.csv')
#assigns the news-sites file location to the variable "inFile" 
outFile = open('output.csv', 'w', newline='')
Compare = open('compare.csv', 'w', newline='')
#assigns the output file location to the variable "outFile"
Writer = csv.writer(outFile)
Reader = csv.reader(inFile)
Check = csv.writer(Compare)
#sets the variable "Reader" to contain the data in "inFile"
#for row in Reader:
	#print('Row #' +str(Reader.line_num)+ '' +str(row))
	#if Reader.line_num ==1:
	#	continue 
	#csvRows.append(row)

#Creating the list where the list of URLs and RSS feeds respectively: 
#are written to the "compare.csv" and "output.csv" file, respectively.
	
#d=feedparser.parse('http://www.reddit.com/r/python/.rss')
#print(d)
#d=feedparser.parse('http://www.wsj.com/xml/rss/3_7014.xml')
#print(d)	
	
Array1 = list(Reader)
for num, name in enumerate(Array1,start = 1):
	Check.writerow([Array1[num-1][1]])
	Writer.writerow([Array1[num-1][2]])
	r=requests.get(Array1[num][2])
	d=feedparser.parse(Array1[num][2])
	#print(Array1[num-1][2])
	#time.sleep(5) 
	#pause code for testing purposes
	#print("Url {}: {}".format(num,name)) 

#print(Array1[2][2])	
#prints RSS feed link in the nth row to test placement of the RSS feed in Array 1

	#Writer.writerow(['Yes'])
	#Testread = open('output.csv')
	#Test = csv.reader(Testread)
	#for row in Test:
	#	print('Row #' +str(Reader.line_num)+ '' +str(row))
	

