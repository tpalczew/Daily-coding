'''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
'''

from typing import List, Optional

class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		m, n = len(nums1), len(nums2)
    		if m > n:
			m, n = n, m # swap arrays 

		t = m + n  # total length
    		left = (m + n + 1) // 2  # length of left half
    		low, high = 0, m

		while low <= high:
        		mid1 = (low + high) // 2
        		mid2 = left - mid1
        	# calculate l1, l2, r1, and r2;
        	l1, l2, r1, r2 = float('-inf'), float('-inf'), float('inf'), float('inf')
        	if mid1 < m:
            		r1 = a[mid1]
        	if mid2 < n:
            		r2 = b[mid2]
        	if mid1 - 1 >= 0:
            		l1 = a[mid1 - 1]
        	if mid2 - 1 >= 0:
            		l2 = b[mid2 - 1]

        	if l1 <= r2 and l2 <= r1:
            		if n % 2 == 1:
                		return max(l1, l2)
            		else:
                		return (float(max(l1, l2)) + float(min(r1, r2))) / 2.0

        	elif l1 > r2:
            		high = mid1 - 1
        	else:
            		low = mid1 + 1
		return 0

# to-do: add tests 
# check the code 



		

			
        


