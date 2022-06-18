'''

In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal 
from top left to bottom right are identical.

Here is an example:

1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2

Write a program to determine whether a given input is a Toeplitz matrix.

'''

matrix = [ [1, 2, 3, 4, 8], [5, 1, 2, 3, 4], [4, 5, 1, 2, 3], [7, 4, 5, 1, 2]  ]

print(matrix)
print("y ", len(matrix))          # number of rows
print("x ", len(matrix[0]))       # number of columns 


def check_diagonal(matrix, x, y):
    value = matrix[y][x]
    x=x+1
    y=y+1
    while (x < len(matrix[0]) and y < len(matrix) ):
        if matrix[y][x] != value:
            return False 
        x=x+1
        y=y+1
    return True 

def solution(matrix):
    for n in range(len(matrix[0])-1):
        if not check_diagonal(matrix, 0, n):
            return False
    
    for m in range(1, len(matrix)):
        if not check_diagonal(matrix, m, 0):
            return False
    return True


matrix = [ [1, 2, 3, 4, 8], 
           [5, 1, 2, 3, 4], 
           [4, 5, 1, 2, 3], 
           [7, 4, 5, 1, 2]  ]

print( solution(matrix) ) 


matrix = [ [1, 2, 3, 3, 3], 
           [5, 1, 2, 3, 4], 
           [4, 5, 1, 2, 3], 
           [7, 4, 5, 1, 2]  ]

print( solution(matrix) ) 


matrix = [ [6, 7, 8],
           [4, 6, 7],
           [1, 4, 6]  ]

print( solution(matrix) )  