'''

reverse sublist 
singly listed list L and two integers s and f as arguments 
s and f inclusive) 

the head node is the first node 
'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class LList:
    def __init__(self):
        self.head = None
    
    # Insert new node
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    
    # print lnkdlist
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    # ---- 

def solution(Lhead, s, f):
    tmp_head = sublist_head = Lhead
    
    for i in range(1, s):
        sublist_head = sublist_head.next 
        
    sub_iter = sublist_head.next
    for k in range(f-s):
        tmp = sub_iter.next
        sub_iter.next, tmp.next, sublist_head.next = tmp.next, sublist_head.next, tmp
    
    return tmp_head.next 


print(" --- (1) ---  ")
llist = LList()
llist.push(2)
llist.push(7)
llist.push(5)
llist.push(3)
llist.push(11)

llist.printList()

solution(llist.head, 1, 3)
print(" ")

llist.printList()

print(" --- (2) ---  ")

llist = LList()
llist.push(8)
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

llist.printList()

solution(llist.head, 4, 7)
print(" ")

llist.printList()