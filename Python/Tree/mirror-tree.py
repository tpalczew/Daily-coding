'''

Given a Binary Tree, convert it into its mirror.


'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None 


def solution(root):
    if (root == None): 
        return
    else:
        temp = root
        solution(temp.left) 
        solution(temp.right)
        temp = root.left 
        root.left = root.right 
        root.right = temp 


def solution2(root):
    if (root == None):
        return
  
    q = []
    q.append(root)
  
    while (len(q)):
        curr = q[0]
        q.pop(0)
        curr.left, curr.right = curr.right, curr.left
        if (curr.left):
            q.append(curr.left)
        if (curr.right):
            q.append(curr.right)


def inorder(node) :
    if (node == None): 
        return
    inorder(node.left) 
    print(node.data, end = " ") 
    inorder(node.right) 


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print(  inorder(root) )

solution(root)

print(  inorder(root) )


root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 

print(  inorder(root) )

solution2(root)

print(  inorder(root) )
