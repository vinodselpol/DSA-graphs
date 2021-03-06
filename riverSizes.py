# create a a final array and visited array withy each element set as false
#then iterate through the matrix and check if elements are visited otherwise 
#traverse the nodes in that matrix using DFS

def riverSizes(matrix):
	sizes=[]
	visited=[[False for value in row] for row in matrix]
	for i in range(len(matrix)):
		for j in range(len(matrix[i])):
			if visited[i][j]:
				continue
			traverse(i, j, matrix, visited, sizes)
	return sizes

def traverse(i, j, matrix, visited, sizes):
	currentSize=0
	nodes=[[i,j]]
	while len(nodes):
		currentNode=nodes.pop()
		i=currentNode[0]
		j=currentNode[1]
		if visited[i][j]:
			continue
		visited[i][j]=True
		if matrix[i][j]==0:
			continue
		currentSize+=1
		unvisited=getUnvisited(i,j, matrix, visited)
		for neighbor in unvisited:
			nodes.append(neighbor)
	if currentSize > 0:
		sizes.append(currentSize)
		
	
	
	
	
def getUnvisited(i, j, matrix, visited):
	unvisited=[]
	if i > 0 and not visited[i-1][j]:
		unvisited.append([i-1,j])
	if i < len(matrix)-1 and not visited[i+1][j]:
		unvisited.append([i+1, j])
	if j > 0 and not visited[i][j-1]:
		unvisited.append([i, j-1])
	if j < len(matrix[0])-1 and not visited[i][j+1]:
		unvisited.append([i, j+1])
	return unvisited
