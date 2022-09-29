'''

Depth First Traversal 

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 

#------------

def solution_InOrder(root):
    result = []
    result = InOrder(root, result)
    return result 

def InOrder(root, result):
    if root:
        # recur on left child
        InOrder(root.left, result)
        result.append(root.data)
        # recur on right child
        InOrder(root.right, result)
    return result 

#------------

def solution_PreOrder(root):
    result = []
    result = PreOrder(root, result)
    return result 

def PreOrder(root, result):
    if root:
        result.append(root.data)
        PreOrder(root.left, result) 
        PreOrder(root.right, result)
    return result 

#------------


def solution_PostOrder(root):
    result = []
    result = PostOrder(root, result)
    return result 

def PostOrder(root, result):
    if root:
        PostOrder(root.left, result)
        PostOrder(root.right, result)
        result.append(root.data)
    return result 

# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

 
'''
            1
           /  \
          2    3 
         / \   / \
        4   5  6  7
 
 # InOrder 

 4 2 5 1 6 3 7  

# PreOrder 

1 2 4 5 3 6 7 

# Post Order

4, 5, 2, 6, 7, 3, 1

'''

print( solution_InOrder(root) )

print( solution_PreOrder(root) )

print( solution_PostOrder(root) )

#---------
# InOrder simple, just print 

def InOrder(root):
    if root:
        InOrder(root.left)
        print(root.data)
        InOrder(root.right)

InOrder(root)