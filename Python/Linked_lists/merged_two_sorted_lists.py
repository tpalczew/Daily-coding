
'''

Merged two sorted lists

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LkdList:
    def __init__(self):
        self.head = None 
    
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
    
def merge(l1, l2):
    tmp = Node(0)
    tail = tmp 
    while True:
        
        # if no more elements of one of the lists go with other 
        if l1 is None:
            tail.next = l2
            break
        if l2 is None:
            tail.next = l1
            break
        
        #
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next 
        else:
            tail.next = l2
            l2 = l2.next 
        
        tail = tail.next 
    
    return tmp.next 
    

llist = LkdList()
llist.push(7)
llist.push(5)
llist.push(2)

#llist.printList()


llist2 = LkdList()
llist2.push(11)
llist2.push(3)

#llist2.printList()


llist.head = merge(llist.head, llist2.head)

llist.printList()
