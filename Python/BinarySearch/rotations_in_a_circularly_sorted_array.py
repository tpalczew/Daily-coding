'''

Given a circularly sorted integer array, find the total number of times the array is rotated.
Assume there are no duplicates in the array, 
and the rotation is in the anti-clockwise direction.


Input:  nums = [8, 9, 10, 2, 5, 6]
Output: The array is rotated 3 times
 
 
Input:  nums = [2, 5, 6, 8, 9, 10]
Output: The array is rotated 0 times

'''

def solution(nums):
    left  = 0
    right =  len(nums) - 1

    while left <= right:
        middle = (left+right)//2

        if nums[left] <= nums[right]:
            return left 
        
        next = (middle + 1) % len(nums)
        prev = (middle - 1 + len(nums)) % len(nums)

        if nums[middle] <= nums[next] and nums[mid] <= nums[prev]:
            return middle
        
        elif nums[middle] <= nums[right]:
            right = middle - 1
        
        elif nums[middle] >= nums[left]:
            left = middle + 1
        
    return -1 


nums = [8, 9, 10, 2, 5, 6]
print( solution(nums) )

nums = [2, 5, 6, 8, 9, 10]
print( solution(nums) )



'''
The time complexity is O( log(n) )
'''
 




