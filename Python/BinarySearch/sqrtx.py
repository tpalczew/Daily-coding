'''
Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.

Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.


Input: x = 4
Output: 2

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.

'''

def solution(x):
    left = 0 
    right = x 
    while left <= right:
        middle = (left+right)//2

        if middle*middle == x:
            return middle 
        elif middle*middle < x: 
            result = middle 
            left = left + 1 
        else:
            right = right -1 
    return result 


x = 4
print( solution(x) )

x = 8
print( solution(x) )

x = 10
print( solution(x) )

x = 25
print( solution(x) )