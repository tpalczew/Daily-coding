
'''

The 24 game is played as follows. 
You are given a list of four integers, each between 1 and 9, in a fixed order. 
By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, 
determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

'''


class Solution:
    def judgePoint24(self, cards):
        return self.allComputeWays(cards, 4, 24)
        
    def allComputeWays(self, nums, l, target):
        if l == 1: # l == length of the array 
            if abs(nums[0] - target) <= 1e-6: # close enough to say that's the right value
                return True
            return False
        
        for first in range(l):
            for second in range(first + 1, l):
                # iterate and pick all pairs from the array 

                tmp1, tmp2 = nums[first], nums[second] # put first and second to temp variables
                
                nums[second] = nums[l - 1] # set second as the last value 

                # set first as any combination of operations on two first / temp variables
                
                nums[first] = tmp1 + tmp2

                # recurse the process 

                if self.allComputeWays(nums, l - 1, target):
                    return True
                nums[first] = tmp1 - tmp2
                
                if self.allComputeWays(nums, l - 1, target):
                    return True
                nums[first] = tmp2 - tmp1
                
                if self.allComputeWays(nums, l - 1, target):
                    return True
                nums[first] = tmp1 * tmp2
                
                if self.allComputeWays(nums, l - 1, target):
                    return True
                if tmp2:
                    nums[first] = tmp1 / tmp2
                    if self.allComputeWays(nums, l - 1, target):
                        return True
                if tmp1:
                    nums[first] = tmp2 / tmp1
                    if self.allComputeWays(nums, l - 1, target):
                        return True
                # backtracking, return original values for first and second 
                nums[first], nums[second] = tmp1, tmp2
        return False


cards = [1, 1, 1, 1]
result = Solution()
print(result.judgePoint24(cards))


cards = [5, 2, 7, 8]
result = Solution()
print(result.judgePoint24(cards))
