def removeIslands(matrix):
    for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			rowIsBorder=row==0 or row==len(matrix)-1
			colIsBorder=col==0 or col==len(matrix[row])-1
			isBorder= rowIsBorder or colIsBorder
			
			if not isBorder:
				continue
			if matrix[row][col] !=1:
				continue
			connectedBorders(row, col, matrix)
	for row in range(len(matrix)):
		for col in range(len(matrix[row])):
			color=matrix[row][col]
			
			if color ==1:
				matrix[row][col]=0
			elif color==2:
				matrix[row][col]=1
	return matrix

def connectedBorders(startRow, startCol, matrix):
	stack=[(startRow, startCol)]
	
	while len(stack) > 0:
		currentPos=stack.pop()
		currentRow, currentCol=currentPos
		
		matrix[currentRow][currentCol]=2
		neighbors=getNeighbor(matrix, currentRow, currentCol)
		for neighbor in neighbors:
			row, col = neighbor
			if matrix[row][col] !=1:
					continue
			stack.append(neighbor)
		
		
def getNeighbor(matrix, row, col):
	neighbors=[]
	
	numsRow=len(matrix)
	numsCol=len(matrix[row])
	if row -1 >=0 :
		neighbors.append((row-1, col))
	if row + 1 < numsRow:
		neighbors.append((row +1, col))
	if col -1 >= 0:
		neighbors.append((row, col -1))
	if col +1 < numsCol:
		neighbors.append((row, col +1 ))
	
	return neighbors
