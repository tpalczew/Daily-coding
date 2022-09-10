'''

Print the nodes in a binary tree level-wise. 

For example, the following should print 1, 2, 3, 4, 5.

  1
 / \
2   3
   / \
  4   5

'''

class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None 
        self.right = None 

def solution(root):
    if not root:
        return 
    result = []
    q = []
    q.append(root)
    while q:
        level = len(q)
        while level > 0:
            tmp = q.pop(0)
            result.append(tmp.data)
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
            level = level -1 
    return result 

root = Node(1);
root.left = Node(2);
root.right = Node(3);
root.right.left = Node(4);
root.right.right = Node(5);

print(solution(root)) 






