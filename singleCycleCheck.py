def hasSingleCycle(array):
    elementsVisited=0
	currentIdx=0
	while elementsVisited < len(array):
		if elementsVisited > 0 and currentIdx ==0:
			return False
		elementsVisited+=1
		currentIdx=getNextIdx(currentIdx, array)
	return currentIdx==0

def getNextIdx(currentIdx, array):
	jump=array[currentIdx]
	nextIdx=(currentIdx +jump)%len(array)
	return nextIdx if nextIdx >=0 else nextIdx + len(array)
