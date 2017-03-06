

import time
import numpy as np

def compareListFast(A1,A2):

	#dictionary specifying the row and column of elements that differ between arrays 1 and 2
	location = []
	
	#dictionary storing the values of whether an element is the same or different
	compare = []
	
	#length of array A1 to check the number of rows
	N=len(A1)
	
	#width of arrays A1 and A2 to check the number of columns
	M1=A1[1][:]
	M2=A2[1][:]
	
	#check that A1 and A2 have same number of columns
	if len(M1) == len(M2):
	
		#check that A1 and A2 have same number of rows
		if len(A1)==len(A2):
		
			#loop through all rows
			for i in range(0,N):
			
				#for the ith row and column 2 (location of the rss feed) store a 1 in compare if they are the same
				if A1[i][2]==A2[i][2]:
					compare.append(1)
					
				#for the ith row and column 2 store a 0 in compare if they are different; store the location 
				elif A1[i][2] != A2[i][2]:
					compare.append(0)
					location.append({i+1})
		
		else:
			print('Please check the length of the lists ')
			return
	else:
		print('Please check the number of elements in each row')
	
	return compare
	
