
'''
Write a function, throw_dice(N, faces, total), 
that determines how many ways it is possible to throw N dice with some number of faces each to get a specific total.

For example, throw_dice(3, 6, 7) should equal 15.

'''

def throw_dice(N, faces, total):
    
    table = [[0]*(total+1) for i in range(faces+1)] # All zeros 
     
    for j in range(1,min( N+1, total+1 )): 
        table[1][j]=1
         
    for i in range( 2, faces + 1 ):
        for j in range( 1 , total+1 ):
            for k in range( 1, min( N +1, j ) ):
                table[i][j] += table[i-1][j-k]
     
    return table[-1][-1]
     
# Driver code
print(throw_dice(4,2,1))
print(throw_dice(2,2,3))
print(throw_dice(6,3,8))
print(throw_dice(4,2,5))
print(throw_dice(4,3,5))

