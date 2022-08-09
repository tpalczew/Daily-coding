'''
Singly linked list 

test for cyclicity

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

    def pprint(self):
        temp = self.head 
        while(temp):
            print(temp.data)
            temp = temp.next

    def check(self):
        '''
        check for cycle 
        '''
        if self.head == None:
            return False
        slow = self.head
        fast = self.head.next
        while slow.data != fast.data:
            if fast == None or fast.next == None:
                return False
            slow = slow.next
            fast = fast.next.next
        return True

llist = LList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)

print("original linked list")
llist.pprint()

print("check for cycle")
print( llist.check() )

llist = LList()
llist.push(4)
llist.push(3)
llist.push(2)
llist.push(1)
llist.push(3)
llist.push(2)
llist.push(1)

print("original linked list")
llist.pprint()

print("check for cycle")
print( llist.check() )





