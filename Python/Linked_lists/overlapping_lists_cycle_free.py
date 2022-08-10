'''

Find if two singly linked lists overlap. 

'''

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next 

class LList:
    def __init__(self):
        self.head = None 
    
    def push(self, newdata):
        tmp = Node(newdata)
        tmp.next = self.head  
        self.head = tmp 
    
    def pprint(self):
        arr_list = []
        tmp = self.head 
        while tmp:
            #print(tmp.data)
            arr_list.append(tmp.data)
            tmp = tmp.next 
        return arr_list

def overlapping(l0, l1):
    def length(llist):
        length = 0 
        while llist:
            length += 1
            llist = llist.next 
        return length 
    l0_len, l1_len = length(l0), length(l1)
    #print("l0_len", l0_len)
    #print("l1_len", l1_len)
    if l0_len > l1_len:
        l0, l1 = l1, l0 # swap so l1 is the longer list 
    
    new_l1_len = length(l1)
    #print("l1_len after swap", new_l1_len)

    for i in range( abs(l0_len - l1_len) ):
        #print(l1.data)
        l1 = l1.next

    #print("l1.data after move ", l1.data)
    
    # now we can start comparing and moving forward 
    while l0 and l1 and l0.data is not l1.data:
        #print(l0.data, l1.data)
        l0, l1 = l0.next, l1.next 
    if l0:
        return True
    else:
        return False

print("")
l0 = LList()
l0.push(11)
l0.push(10)
l0.push(9)
l0.push(8)
l0.push(5)
l0.push(3)
l0.push(1)

print(l0.pprint())

print("")
l1 = LList()
l1.push(11)
l1.push(10)
l1.push(9)
l1.push(8)
l1.push(2)
print(l1.pprint())

print( overlapping(l0.head, l1.head) )


#------------------- no overlapping 

print("")
l0 = LList()
l0.push(11)
l0.push(10)
l0.push(9)
l0.push(8)
l0.push(5)
l0.push(3)
l0.push(1)

print(l0.pprint())

print("")
l1 = LList()
l1.push(13)
l1.push(12)
l1.push(10)
l1.push(9)
l1.push(2)
print( l1.pprint() ) 

print( overlapping(l0.head, l1.head) )






