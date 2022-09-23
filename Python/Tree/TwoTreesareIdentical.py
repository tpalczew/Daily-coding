'''
Given two binary trees, the task is to find if both of them are identical or not. 

Example 2:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: Yes
Explanation: There are two trees both
having 3 nodes and 2 edges, both trees
are identical having the root as 1,
left child of 1 is 2 and right child
of 1 is 3.
Example 2:

Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: No
Explanation: There are two trees both
having 3 nodes and 2 edges, but both
trees are not identical.

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None 
        self.right = None 


def solotion(root1, root2):
    if root1 == None and root2 == None:
        return True 
    else:
        if root1 is not None and root2 is not None:
            return root1.data == root2.data and solotion(root1.left, root2.left) and solotion(root1.right, root2.right)
    return False


root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

print( solotion(root1, root2) )



root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
 
root2.left = Node(2)
root2.right = Node(3)
root2.left.right = Node(5)

print( solotion(root1, root2) )