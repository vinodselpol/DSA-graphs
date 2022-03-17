# create two empty data staructures filled with false
# use recursive calls

def cycleInGraph(edges):
    numberOfNodes=len(edges)
	visited=[False for _ in range(numberOfNodes)]
	stack=[False for _ in range(numberOfNodes)]
	
	for node in range(numberOfNodes):
		if visited[node]:
			continue
		
		containsCycle=nodeInCycle(node, edges, visited, stack )
		if containsCycle:
			return True
		
	return False


def nodeInCycle(node, edges, visited, stack):
	visited[node]=True
	stack[node]=True
	
	neighbors=edges[node]
	for neighbor in neighbors:
		if not visited[neighbor]:
			containsCycle=nodeInCycle(neighbor, edges, visited, stack)
			if containsCycle:
				return True
		elif stack[neighbor]:
				return True
			
	stack[node]=False
	return False
