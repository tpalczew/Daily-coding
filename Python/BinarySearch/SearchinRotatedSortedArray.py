'''

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
(1 <= k < nums.length) such that the resulting array is 

[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 

For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, 
return the index of target if it is in nums, 
or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.


Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1

'''

def solution(nums, target):
    left = 0 
    right = len(nums)-1
    
    while left <= right:
        
        middle = (left+right) // 2

        if nums[middle] == target:
            return middle 
        
        if nums[left] < nums[middle]:
            # sorted left side 
            if target < nums[middle] and target >= nums[left]:
                right = middle - 1
            else:
                left = middle + 1

        else:
            # sorted right side 
            if target > nums[middle] and target <= nums[right]:
                left = middle + 1
            else:
                right = middle - 1 
    return -1 


nums = [4,5,6,7,0,1,2]
target = 0

print(solution(nums, target))


nums = [4,5,6,7,0,1,2]
target = 3

print(solution(nums, target))


