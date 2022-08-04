'''

Determine whether a doubly linked list is a palindrome. 

What if it’s singly linked?

For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.


palindrome = a word, phrase, or sequence that reads the same backward as forward

'''

'''
# ---- SLL
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
'''
# --- for SLL we can do stack 



# ---- DLL
class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class dll:
    def __init__(self):
        self.head = None

    def push(self, new_data):
        # 1 & 2: Allocate the Node & Put in the data
        new_node = Node(data = new_data)
  
        # 3. Make next of new node as head and previous as NULL
        new_node.next = self.head
        new_node.prev = None
  
        # 4. change prev of head node to new node 
        if self.head is not None:
            self.head.prev = new_node
  
        # 5. move the head to point to the new node
        self.head = new_node 

    def solution(self):
        if self.head == None:
            return True
        left = self.head
        right = left
        while right.next != None:
            right = right.next
        # we just went to the end ot the list 
    
        while left != right:     # if left == right we are in the middle as we will increase left and decrease right 
            if left.data != right.data: # data pairs need to be equal 
                return False
            left = left.next
            right = right.prev
        # we are here, it means that palindrome 
        return True


head = dll()

head.push(1)
head.push(4)
head.push(3)
head.push(4)
head.push(1)

if head.solution():
    print("True")
else:
    print("False")


head = dll()

head.push(1)
head.push(4)

if head.solution():
    print("True")
else:
    print("False")

