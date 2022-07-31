'''

You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) r
epresenting a polygon. 
You can assume these points are given in order; that is, 
you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so on, 
finally looping around to connect point N to point 1.

Determine if a new point p lies inside this polygon. 
(If p is on the boundary of the polygon, you should return False).


'''
import math
import numpy as np

def get_angle(vector_1, vector_2):
    unit_vector_1 = vector_1 / np.linalg.norm(vector_1)
    unit_vector_2 = vector_2 / np.linalg.norm(vector_2)
    dot_product = np.dot(unit_vector_1, unit_vector_2)
    angle = np.arccos(dot_product)
    return angle


def solution(pol, point):
    angle = 0 
    for index in range(len(pol)-1):
        p1_h = pol[index][0] - point[0]
        p1_v = pol[index][1] - point[1]
        p2_h = pol[(index+1)][0] - point[0]
        p2_v = pol[(index+1)][1] - point[1]
        vector_1 = [p1_h,p1_v]
        vector_2 = [p2_h,p2_v]
        angle += get_angle(vector_1, vector_2)
    if (abs(angle) < math.pi):
        return(False)
    else:
        return(True)


pol = [ (0, 0), (10, 0), (10, 10), (0, 10) ]
p = (20, 20)

print( solution(pol, p) )

p = (5, 5)

print( solution(pol, p) )

pol = [ (0, 0), (5, 0), (5, 5), (3, 3) ] 
p = (3, 3)

print( solution(pol, p) )

p = (5, 1)

print( solution(pol, p) )

p = (8, 1)
print( solution(pol, p) )

pol = [ (0, 0), (10, 0), (10, 10), (0, 10) ]
     
p = (-1, 10)

print( solution(pol, p) )

'''
No 
Yes 
Yes 
Yes 
No 
No 
'''
