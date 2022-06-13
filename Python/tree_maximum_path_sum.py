'''

Given a binary tree of integers, 
find the maximum path sum between two nodes. 
The path must go through at least one node, and does not need to go through the root.

'''

# class for tree's node, -> data = value, left and right  

class Node:     
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# find max function 

def findMax(root):
    if root is None:
        return 0 
    
    left = findMax(root.left)
    right = findMax(root.right)

    max_single = max( max(left, right) + root.data, root.data) 
    ''' max between root node and root node + left or root node + right depending if left or right is bigger 
    '''
    max_top = max( max_single , left + right + root.data)
    '''
    '''
    findMax.res = max( findMax.res, max_top ) # final result 
    return max_single 

def solution(root):
    findMax.res = -1.0
    findMax(root)
    return findMax.res

#------


root = Node(100)
root.left = Node(25)
root.right   = Node(70)
root.left.left  = Node(37)
root.left.right = Node(1)
root.right.right = Node(-90)
root.right.right.left   = Node(57)
root.right.right.right  = Node(99)

print(solution(root))

