'''

A girl is walking along an apple orchard with a bag in each hand. 
She likes to pick apples from each tree as she goes along, 
but is meticulous about not putting different kinds of apples in the same bag.

Given an input describing the types of apples she will pass on her path, in order, 
determine the length of the longest portion of her path that consists of just two types of apple trees.

For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, 
with a length of four.

'''

def solution(arr):
    len_arr = len(arr)
    if len_arr < 3:
        return len_arr 
    seen_apples = []
    paths = [] 
    maxp = 1 
    for ind in range(0, len_arr-1):     
        f = arr[ind]
        fp = arr[ind+1]
        seen_apples.append(f)
        seen_apples.append(fp)
        s = list(set(seen_apples))      
        if len(s) <= 2:
            maxp += 1  
            if ind == len_arr-2:
                paths.append(maxp)
        else:
            paths.append(maxp)
            maxp = 1
            seen_apples = []    
    return max(paths)

arr = [2,1,2,3,3,1,3,5]
print(solution(arr))
            
arr2 = [2,1,2,2,2,2,1,1,2,2,3,3,1,3,5]
print(solution(arr2))

arr3 = [2,1,2,2,2,2,1,1,2,2,3,3,1,3,5,5,5,5,5,5,5,5,5,5,7,7,7,7,7,7,7,7,7,7,7,7,7,5,5,5,5]
print(solution(arr3))

arr4 = [1,1]
print(solution(arr4))

arr5 = [1,1,2]
print(solution(arr5))

arr6 = [7]
print(solution(arr6))

arr7 = [7,7,7,7,7,7,7,7,7,7,7,7,7,90]
print(solution(arr7))

arr8 = [7,7,7,7,7,7,7,7,7,7,7,7,7]
print(solution(arr8))