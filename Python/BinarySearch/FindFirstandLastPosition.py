'''

Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.


Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Input: nums = [], target = 0
Output: [-1,-1]

'''


def search(nums, target, flag):
    left = 0 
    right = len(nums)-1 
    ind = -1
    while left <= right:        
        middle = (left + right) // 2 
        if nums[middle] < target:
            left = middle + 1
        elif nums[middle] > target:
            right = middle -1 
        else:
            ind = middle 
            if flag:
                right = middle - 1
            else:
                left = middle + 1         
    return ind


def solution(nums, target):
    left_ind = search(nums, target, True)
    right_ind = search(nums, target, False )
    return [left_ind, right_ind]


nums = [5,7,7,8,8,10]
target = 8

print(solution(nums, target))

nums = [5,7,7,8,8,8,8,8,10]
target = 8

print(solution(nums, target))


nums = [5,7,7,8,8,10]
target = 6

print(solution(nums, target))


nums = []
target = 0           

print(solution(nums, target))

        
            
        




