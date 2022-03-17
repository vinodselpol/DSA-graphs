# first get all positions of positive values. store it in a queue and create another
# queue to store all converted negatuve values. 
# once we know pos of positive values, determine its neighbors using bfs
# check if neighbors are negative, then convert into positive and append into empty stack
# after each tie we fill a queue, increment the passes by 1



def minimumPassesOfMatrix(matrix):
    passes=convertNegative(matrix) 
	return passes-1 if not containsNegative(matrix) else -1
	
	
def convertNegative(matrix):
	nextPassQueue=positivePos(matrix)
	passes=0
	while len(nextPassQueue) >0:
		currentPass=nextPassQueue
		nextPassQueue=[]
		
		while len(currentPass) >0 :
			currentPos=currentPass.pop(0)
			currentRow, currentCol=currentPos
			
			adjacentPos=getAdjacentPos(currentRow, currentCol, matrix)
			
			for neighbor in adjacentPos:
				row, col =neighbor
				
				if matrix[row][col] <0:
					matrix[row][col]*=-1
					nextPassQueue.append([row, col])
		passes+=1
	return passes
				
			
			
def getAdjacentPos(row, col, matrix):
	adjacentPos=[]
	
	if row > 0:
		adjacentPos.append([row-1, col])
		
	if row < len(matrix)-1:
		adjacentPos.append([row+1, col])
	
	if col > 0:
		adjacentPos.append([row, col-1])
		
	if col < len(matrix[0])-1:
		adjacentPos.append([row, col+1])
		
	return adjacentPos
			
			
	
	
def positivePos(matrix):
	positivePos=[]
	
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			value=matrix[row][col]
			
			if value > 0:
				positivePos.append([row, col])
	return positivePos


def containsNegative(matrix):
	for row in matrix:
		for val in row:
			if val <0:
				return True
	return False
