'''

Number is represented in linked list such that each digit corresponds to a node in linked list. 
Add 1 to it. For example 1999 is represented as (1-> 9-> 9 -> 9) 
and adding 1 to it should change it to (2->0->0->0) 


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
        llp = []
        tmp = self.head 
        while tmp:
            llp.append(tmp.data)
            tmp = tmp.next 
        print(llp)
    
    def reverse(self):
        prev = None
        current = ll.head 
        while current is not None:
            next = current.next 
            current.next = prev 
            prev = current 
            current = next
        self.head = prev  
        

def solution(ll):
    ll.lprint()
    ll.reverse()
    ll.lprint()  

    llk = ll
    hd = ll 
    
    carry = 0
    prev = None
    
    hd.head.data += 1

    while(hd.head != None) and (hd.head.data > 9 or carry > 0):
        print("data ", hd.head.data)
        prev = hd.head
        hd.head.data += carry
        carry = hd.head.data // 10
        print("carry ", carry)
        hd.head.data = hd.head.data % 10
        hd.head = hd.head.next


    # TO-DO: fix 1999 -> 2000 
  
    if carry > 0:
        prev.next = Node(carry)
    
    llk.reverse()
    llk.lprint()

ll = Llist()
ll.push(8)
ll.push(9)
ll.push(9)
ll.push(1)

solution(ll)


ll = Llist()
ll.push(5)
ll.push(4)
ll.push(3)
ll.push(3)
ll.push(2)
ll.push(1) 

solution(ll)


ll = Llist()
ll.push(9)
ll.push(9)
ll.push(9)
ll.push(1)

solution(ll)