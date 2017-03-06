def InitializeArray(N,M):

	#initialize array to be output
	A4 = list()
	
	#intitialize intermediate array to append to final array
	A3 = list()

	#create a row of M zeros
	for k in range (0,M):
		A3.append('0',)
		
	#append N rows of size 1xM row vector of zeros
	for i in range (0,N):
		A4.append(A3)
		
	#A4 is now an NxM array of zeros
	return A4		