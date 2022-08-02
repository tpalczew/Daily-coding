
'''
Given the head of a singly linked list, 

swap every two nodes and return its head.

For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None 
    
    def solution(self):
        temp = self.head 
        if temp is None:
            return 
        while temp and temp.next:
            if temp.data!= temp.next.data:
                # swap
                temp.data, temp.next.data = temp.next.data, temp.data 
            temp = temp.next.next
    # Finsert new node
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



llist = LinkedList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("original linked list")
llist.printList()

llist.solution()

print("swap every two nodes")
llist.printList()

print("head")
print(llist.head.data)




