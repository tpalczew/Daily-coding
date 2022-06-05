'''
Given a 2-D matrix representing an image, a location of a pixel in the screen and a color C, 
replace the color of the given pixel and all adjacent same colored pixels with C.

For example, given the following matrix, and location pixel of (2, 2), and 'G' for green:

B B W
W W W
W W W
B B B
Becomes
B B G
G G G
G G G
B B B

'''

# We can use recursion

g_matrix = [['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']]
print(g_matrix)
position = [2,2]
target_matrix = g_matrix = [['B', 'B', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G'], ['B', 'B', 'B']]

def check_all(g_matrix, x, y, target, new_color, max_x, max_y):
    if not g_matrix:
        return []
    if x<0 or x> max_x or y<0 or y>max_y or g_matrix[y][x] != target or g_matrix[y][x] == new_color:
        return g_matrix
    g_matrix[y][x] = new_color
    check_all(g_matrix, x+1, y, target, new_color, max_x, max_y)
    check_all(g_matrix, x, y, target, new_color, max_x, max_y)
    check_all(g_matrix, x-1, y, target, new_color, max_x, max_y)
    check_all(g_matrix, x, y-1, target, new_color, max_x, max_y)

def solution(g_matrix, position, new_color):
    target = g_matrix[position[0]][position[1]]
    max_x = len(g_matrix[0])-1
    max_y = len(g_matrix)-1
    if(target==new_color):
      return g_matrix
    g_matrix = check_all(g_matrix, position[1], position[0], target, new_color, max_x, max_y)
    return g_matrix

print(solution(g_matrix, position, 'G'))

'''
[['B', 'B', 'W'], ['W', 'W', 'W'], ['W', 'W', 'W'], ['B', 'B', 'B']]
[['B', 'B', 'G'], ['G', 'G', 'G'], ['G', 'G', 'G'], ['B', 'B', 'B']]
'''

# We can also use BFS approach but will do this another day. 