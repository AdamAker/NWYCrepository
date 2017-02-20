import time
import numpy as np

def compareList(A1,A2):
	location = []
	N=len(A1)
	M1=A1[1][:]
	M2=A2[1][:]
	if len(M1) == len(M2):
		if len(A1)==len(A2):
			for i in range(0,N):
				for j in range(0,len(M1)):
					if A1[i][j]==A2[i][j]:
						compare = 1
					elif A1[i][j] != A2[i][j]:
						compare = 0
						location.append({i+1:j+1})
		
		else:
			print('Please check the length of the lists ')
			return
	else:
		print('Please check the number of elements in each row')
	print(location)