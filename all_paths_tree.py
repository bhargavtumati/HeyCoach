
# Python program to print all paths from root to leaf in a binary tree

class Node:         #binary tree node contains data field ,  left and right pointer
	def __init__(self, data):          # constructor to create tree node
		self.data = data
		self.left = None
		self.right = None

def printPaths(root):      # function to print all path from root to leaf in binary tree list to store path
	path = []
	printPathsRec(root, path, 0)

def printPathsRec(root, path, pathLen):      #Helper function to print path from root to leaf in binary tree
	
	if root is None:    #Base condition - if binary tree is empty return
		return

	if(len(path) > pathLen): #add current root's data into path_ar list if length of list is gre
		path[pathLen] = root.data
	else:
		path.append(root.data)

	pathLen = pathLen + 1     # increment pathLen by 1

	if root.left is None and root.right is None:
		print(path)     # leaf node then print the list
		  
	else:
		printPathsRec(root.left, path, pathLen)     # try for left and right subtree
		printPathsRec(root.right, path, pathLen)



# Driver program to test above function

root = Node(10)   
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(2)

printPaths(root)

"""
Constructed binary tree is 
			10
		/ \
		8	 2
    / \      /
	3 5     2
"""
# This code has been contributed by Shweta Singh.
