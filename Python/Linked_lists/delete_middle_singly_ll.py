
'''

Given a singly linked list, delete middle of the linked list. 
For example, if given linked list is 1->2->3->4->5 
then linked list should be modified to 1->2->4->5.
If there are even nodes, then there would be two middle nodes, 
we need to delete the second middle element. 
For example, if given linked list is 1->2->3->4->5->6 then it 
should be modified to 1->2->3->5->6.
If the input linked list is NULL or has 1 node, 
then it should return NULL

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class Llist:
    def __init__(self):
        self.head = None 
    
    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head
        self.head = newnode 
    
    def lprint(self):
        tmp = self.head
        llprint = []
        while tmp:
            llprint.append(tmp.data)
            tmp = tmp.next
        return llprint  

def solution(ll):
    tmp = ll.head 
    if tmp is None or tmp.next is None:
        return None 
    slow = fast = ll.head
    result = []
    while fast and fast.next:
        result.append(slow.data)
        slow = slow.next 
        fast = fast.next.next 
    slow = slow.next 
    while slow:
        result.append(slow.data)
        slow = slow.next 
    final = Llist()
    [final.push(elm) for elm in result[::-1]]
    return final 


print("create singly linked list")
ll = Llist()
print("done")

print("push some data")
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1) 
print("done")

print("our list")
print( ll.lprint() ) 

print("delete middle element")
new = solution(ll)
print( new.lprint() )


print("create singly linked list")
ll = Llist()
print("done")

print("push some data")
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(2)
ll.push(1) 
print("done")

print("our list")
print( ll.lprint() ) 

print("delete middle element")
new = solution(ll)
print( new.lprint() )