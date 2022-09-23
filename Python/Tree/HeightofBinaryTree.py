'''

Height of Binary Tree

Given a binary tree, find its height.

Input:
     1
    /  \
   2    3
Output: 2

Input:
  2
   \
    1
   /
 3
Output: 3   


root = newNode(1)                         # 1 

root.left = newNode(12)                   # 2
root.right = newNode(13)
 
root.right.left = newNode(14)             # 3 
root.right.right = newNode(15)
 
root.right.left.left = newNode(21)        # 4 
root.right.left.right = newNode(22)
root.right.right.left = newNode(23)
root.right.right.right = newNode(24)

Output: 4 


Expected Time Complexity: O(N)
Expected Auxiliary Space: O(N)
'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None 


def solution(root):
    if not root:
        return 0 
    else:    
        leftdepth = solution(root.left)
        rightdepth = solution(root.right) 

        if leftdepth >= rightdepth:
            return leftdepth+1
        else:
            return rightdepth+1 

def solution2(root):
    if not root:
        return 0
    else:
        q = []
        q.append(root)
        q.append(None)
        h = 0 
        while len(q)>0:
            temp = q[0]
            q = q[1:]
            if temp==None:
                h+=1
            if not temp==None:
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right) 
            elif len(q)>0:
                q.append(None)
    return h  





root = Node(1)
root.left = Node(2)
root.right = Node(3)
 
print (solution(root))

print (solution2(root))

root = Node(2)
root.right = Node(1)
root.right.left = Node(3) 

print (solution(root))

print (solution2(root))


root = Node(1)
root.left = Node(12)
root.right = Node(13)
 
root.right.left = Node(14)
root.right.right = Node(15)
 
root.right.left.left = Node(21)
root.right.left.right = Node(22)
root.right.right.left = Node(23)
root.right.right.right = Node(24)


print (solution(root))
print (solution2(root))