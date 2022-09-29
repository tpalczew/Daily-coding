
'''

Level Order Binary Tree Traversal

BFS - Breadth First Traversal 


            1
            /\
           2  3
          /\  /\
         4  5 6 7

Output: 1 2 3 4 5 6 7     

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def BFSTree(root, result):
    if root is None:
        return 
    q = []
    q.append(root)

    while( len(q) > 0 ):
        result.append(q[0].data)
        node = q.pop(0)
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return result 

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

result = []
print( BFSTree(root, result) ) 
