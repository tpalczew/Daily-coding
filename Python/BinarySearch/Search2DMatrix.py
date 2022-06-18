'''

Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. 

This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

'''

def solution(matrix_, target_):
    array_ = []
    for row in matrix_:
        array_.extend(row)
    left = 0
    right = len(array_)-1    
    while left <= right:
        middle = (left + right) // 2
        if array_[middle] == target_:
            return True
        elif array_[middle] < target_:
            left = middle + 1
        else:
            right = middle - 1
    return False 

matrix_ = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target_ = 3

print( solution(matrix_, target_) )

matrix_ = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]

target_ = 13

print( solution(matrix_, target_) )
