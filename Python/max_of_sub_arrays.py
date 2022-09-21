'''

Given an array of integers and a number k, 
where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] 
and k = 3, we should get: [10, 7, 8, 8], since:

n = 6 
k = 3 

10 = max(10, 5, 2)    # indices [0, k-1]  
7 = max(5, 2, 7)      #         [0+1, k]
8 = max(2, 7, 8)      #         [0+2, k+1]
8 = max(7, 8, 7)      #         [0+3, k+2]

Do this in O(n) time and O(k) space. 
You can modify the input array in-place and you do not need to store the results. 
You can simply print them out as you compute them.


'''

arr = [10, 5, 2, 7, 8, 7] 

def solution(arr, k):
    n = len(arr)
    result = []
    while k + len(arr)-n <= len(arr):
        m = 0 
        for elem in arr[len(arr)-n : k + len(arr)-n ]:
            if elem > m:
                m = elem 
        print(m)
        result.append(m)
        n = n - 1
    return result

# --- 
k = 3
print( solution(arr, k) )


# --- that's a good starting point, how can we get to the O(n) and O(k) 

'''
Dequeu 
'''





