
'''

Given an integer n and a list of integers l, 
write a function that randomly generates a number from 0 to n-1 
that isn't in l (uniform).


n = 7
l = {0, 1, 5}

the function should return any random number { 2, 3, 4, 6 } with equal probability.
'''

import random
class Solution:
    def __init__(self, n, blacklist):
        self.blacklist = [-1]+sorted(blacklist)+[n]
        self.whites = n - len(blacklist)
    def pick(self):
        r = random.randint(1, self.whites)
        left, right = 0, len(self.blacklist)-1
        while left < right:
            m = (left + right)//2
            whites = self.blacklist[m] + 1 - m
            if whites >= r:
                right = m - 1
            else:
                if whites + self.blacklist[m+1] - self.blacklist[m] - 1 >= r:
                    left = m
                    break
                left = m + 1
        return r + left - 1

n = 7
l = {0, 1, 5}
sol = Solution(n,l)
print( sol.pick() ) 

# { 2, 3, 4, 6 } 
counter = {} 
counter[2], counter[3], counter[4], counter[6] = 0, 0, 0, 0

for elem in range(10000000):
    a = sol.pick()
    counter[a] = counter[a] + 1

print(counter)