
'''
Add Two Numbers

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]

'''

from typing import Optional

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next



def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		#
		d = ListNode()
		c = 0 
		temp = d
		
		while l1 or l2 or c:
			if l1:
				val1 = l1.val
			else:
				val1 = 0
			if l2:
				val2 = l2.val
			else:
				val2 = 0
			t = val1 + val2 + c 
			c = t // 10
			v = t % 10
			
			temp.next = ListNode()
			temp = temp.next 

			if l1:
				l1.next
			if l2:
				l2.next 
		return d.next 


l1 = ListNode()
l1.val = 2
l1.next = ListNode()
l1.next.val = 4
l1.next.next = ListNode()
l1.next.next.val = 3

l2 = ListNode()
l2.val = 5
l2.next = ListNode()
l2.next.val = 6
l2.next.next = ListNode()
l2.next.next.val = 4


result = addTwoNumbers(l1, l2)

print(result)
			
			
        
