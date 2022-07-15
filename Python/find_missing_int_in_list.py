
'''

Given an array of integers, 
find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. 
The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.



#------------   https://www.youtube.com/watch?v=_OAFHDVihjo  --------------

'''

inp = [-7,-6,-8,5,6,-1,3,4,-1,1] 
# out = 2 

inp2 = [1,2,0]
# out = 3 

def solution(inp):
    inps = list(sorted(inp))
    for ind, elem in enumerate(inps):
        if elem > 0:
            if ind+1 <= len(inps)-1:
                if inps[ind+1] != elem+1:
                    return elem+1
            else:
                return elem+1

print(solution(inp))
print(solution(inp2))

# Not in linear time and constant space.  



