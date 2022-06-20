'''

Given a positive integer n, find the smallest number of squared integers which sum to n.

For example, given n = 13, return 2 since 13 = 3^2 + 2^2 = 9 + 4.

Given n = 27, return 3 since 27 = 3^2 + 3^2 + 3^2 = 9 + 9 + 9.

'''


n = 27

def solution(n):
    if n <= 3:
        return n 
    rest = n 
    for elem in range(1, n-1):
        temp = elem*elem
        if temp > n:
            break 
        else:
            rest = min(rest, 1 + solution(n - temp) )
        
    return rest 

print( solution(n) )

# time complexity is exponential 

'''
You can do this with 1) dynamic programming (dp) 
2) dp + memoization, 3) dp bottom-up, and 4) graph BFS 
'''





