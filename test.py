import csv
from compareList import compareList 

inFile1 = open('news-sites.csv')
Reader1 = csv.reader(inFile1)
A1 = list(Reader1)

inFile2 = open('news-sites2.csv')
Reader2 = csv.reader(inFile2)
A2 = list(Reader2)



a=compareList(A1,A2)