'''
Implement cyclic right shift for singly linked list

inputs
singly linked list 
k - a nonnegative integere 

'''
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class llist:
    def __init__(self):
        self.head = None 
    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head 
        self.head = newnode 
    def prnt(self):
        l = self.head
        ll = []
        while l:
            ll.append(l.data)
            l = l.next
        return ll
#---
def solution(L, k):
    tail, n = L, 1
    while tail.next:
        n+=1             # number of nodes in the list 
        tail = tail.next # the last node 
    k %= n # k = k % n  ; Modulus - remainder of the division of left operand by the right
    if k:
        tail.next = L  # we connect tail node to the head -> cycle 
        steps, newtail = (n-k), tail  # new head will be (n-k)th node
        while steps:
            steps -= 1
            newtail = newtail.next 
        newhead = newtail.next
        newtail.next = None
        return newhead

llist = llist()
llist.push(7)
llist.push(6)
llist.push(5)
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
print(llist.prnt())

k = 2
print(k)
h = ( solution(llist.head, k) )
hh = [] 
while h:
    hh.append(h.data)
    h = h.next
print(hh)
