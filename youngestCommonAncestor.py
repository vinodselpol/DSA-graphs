# This is an input class. Do not edit.

# first find out the depths of both descendants
# if the diff between depths is greater than 0
#bring the lower descendant to same level with other descendant
# then we check if both values are same otherwise come up one level untill they are same
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None


def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
	depthOne=getDepth(descendantOne, topAncestor)
	depthTwo=getDepth(descendantTwo, topAncestor)
	
	if depthOne > depthTwo:
		return backtrackAncestor( descendantOne, descendantTwo, depthOne-depthTwo)
	else:
		return backtrackAncestor( descendantTwo, descendantOne, depthTwo-depthOne)
		
	
	
def getDepth(descendant, topAncestor):
	depth=0
	while descendant != topAncestor:
		depth+=1
		descendant=descendant.ancestor
	return depth

def backtrackAncestor( lowerDescendant, higherDescendant, diff):
	while diff >0:
		lowerDescendant=lowerDescendant.ancestor
		diff-=1
		
	while lowerDescendant != higherDescendant:
		lowerDescendant=lowerDescendant.ancestor
		higherDescendant=higherDescendant.ancestor
		
	
	return lowerDescendant
