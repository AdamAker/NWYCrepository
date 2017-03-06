import csv
from compareListFast import compareListFast 
from OutputAppend import OutputAppend
from InitializeArray import InitializeArray
import json
import time


#Load new-sites.csv into an array A1
inFile1 = open('news-sites.csv')
Reader1 = csv.reader(inFile1)
A1 = list(Reader1)

#Load news-sites2.csv into an array A2
inFile2 = open('news-sites2.csv')
Reader2 = csv.reader(inFile2)
A2 = list(Reader2)

N = len(A1)
M = len(A1[1][:])
A4 = InitializeArray(N,M)
#print(N)
#print(M)
#print(A4[1][2])
#print(type(A4[1][2]))

#Compare both arrays to find differences
x = compareListFast(A1,A2)

a=94
print(len(x))
#print(len(A4))
#print(len(A4[1][:]))
#print(x[a])
#print(A1[1][1])
#print(A4[1][1])
#print(type(A4))

#Append output based on whether A1 or A2 is different
for k in range(0,len(x)):

	#call append function
	if x[k] == 0:
		A4[k] = A1[k]
		print('change')
		time.sleep(1)
		continue
	#skip
	elif x[k] == 1:
		print('same')
		time.sleep(1)
		continue
		
#print(A4[a][:])
#print(A1[a][:])
print(A4[a][2])
print(type(A4[a][2]))
#print(A4[100][2])
#print(type(A4[100][2]))

#y = OutputAppend(A1)

#print(y)
#print(json.dumps(y, sort_keys=True, indent=4 * ' '))