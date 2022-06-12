

def binarySearch(arr, target):
    left = 0              # first index 
    right = len(arr) - 1  # last index
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle, target 
        elif arr[middle] < target:
            left = middle + 1 
        elif arr[middle] > target:
            right = middle - 1
    return -1 

arr = [1,2,3,4,5,6,7,8,9,10,12,15,17,19,21,25,27,30]
target = 17 

print( binarySearch(arr, target) )


# ---- recursive 


'''
[ --target ---------------------- ]

1st)  [-- target ----] middle [----------] 
      left = 0        right = middle -1     # if arr[middle] > target 

      [- middle target -]
      left = 0    right = middle + 1        # if arr[middle] < target 

      middle = target -> return 
'''


def binarySearch(arr, target, left, right):
    if left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
                return middle, target 
        elif arr[middle] < target:
            return binarySearch(arr, target, middle + 1, right)
        elif arr[middle] > target:
            return binarySearch(arr, target, left, middle - 1)
        return -1 

def solution(arr, target):
    left = 0
    right = len(arr) -1 
    return binarySearch(arr, target, left, right)
    

#------------------------------------------------

arr = [1,2,3,4,5,6,7,8,9,10,12,15,17,19,21,25,27,30]
target = 17 

print( solution(arr, target) )



arr = [1,2,3,4,5,6,7,8,9,10,12,15,17,19,21,25,27,30]
target = 1

print( solution(arr, target) )

arr = [1,2,3,4,5,6,7,8,9,10,12,15,17,19,21,25,27,30]
target = 30

print( solution(arr, target) )

arr = [1,2,3,4,5,6,7,8,9,10,12,15,17,19,21,25,27,30]
target = 3

print( solution(arr, target) )

#--------------------------