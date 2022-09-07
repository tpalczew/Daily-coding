
'''

Given a singly linked list consisting of N nodes. 
The task is to remove duplicates (nodes with duplicate values) 
from the given list (if exists).
Note: Try not to use extra space. 
Expected time complexity is O(N). 
The nodes are arranged in a sorted way.


Input:
LinkedList: 2->2->4->5
Output: 2 4 5
Explanation: In the given linked list 
2 ->2 -> 4-> 5, only 2 occurs more 
than 1 time.

Input:
LinkedList: 2->2->2->2->2
Output: 2
Explanation: In the given linked list 
2 ->2 ->2 ->2 ->2, 2 is the only element
and is repeated 5 times.

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

def solution(ll):    
    current = ll.head
    while current.next:
        if current.data == current.next.data:
            nextNext = current.next.next
            current.next = nextNext
        else:
            current = current.next        
    return ll.head

l0 = LList()
l0.push(11)
l0.push(10)
l0.push(9)
l0.push(8)
l0.push(1)
l0.push(1)
l0.push(1)

l0.lprint()

tmp = solution(l0)

while tmp:
    print(tmp.data)
    tmp = tmp.next