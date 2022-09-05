
'''

Given a singly linked list, find the middle of the linked list. 
For example, if the given linked list is 1->2->3->4->5 then the output should be 3. 

If there are even nodes, then there would be two middle nodes, 
we need to print the second middle element. 
For example, if the given linked list is 1->2->3->4->5->6 then the output should be 4. 

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class LList:
    def __init__(self):
        self.head = None 
    
    def push(self, newdata):
        newnode = Node(newdata)
        newnode.next = self.head 
        self.head = newnode 
    
    def lprint(self):
        tmp = self.head
        nodesdata = []
        while tmp:
            nodesdata.append(tmp.data)
            tmp = tmp.next 
        return nodesdata

'''
1->2->3->4->5
'''

import math 

def solution(ll):
    tmp = ll.head 
    tmp2 = ll.head 
    length = 0
    while tmp:
        length+=1
        tmp = tmp.next 
    middle = math.ceil(length/2)
    for i in range(middle):
        tmp2 = tmp2.next
    return tmp2.data 


#----- 

'''
1->2->3->4->5
Output = 3 
'''

print("create singly linked list")
ll = LList()
print("done")

print("push some data")
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(3)
ll.push(2)
ll.push(1) 
print("done")

print("our list")
print( ll.lprint() ) 

print("find middle element")
print(solution(ll))

'''
1->2->3->4->5->6 
Output = 4
'''

print("create singly linked list")
ll = LList()
print("done")

print("push some data")
ll.push(6)
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(3)
ll.push(2)
ll.push(1) 
print("done")

print("our list")
print( ll.lprint() ) 

print("find middle element")
print(solution(ll))