'''
Rotate an array of n elements to the right by k steps.
'''

arr_n = [1,2,3,4,5,6]

def solution(arr_n, k):
    w = len(arr_n) - k
    print(w)
    left  = arr_n[:w]
    right = arr_n[w:]
    left_rev  = left[::-1]
    right_rev = right[::-1]
    left_rev.extend(right_rev)
    return left_rev[::-1]

print( solution(arr_n, 2) )
