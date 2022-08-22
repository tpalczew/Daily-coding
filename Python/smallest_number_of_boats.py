'''
An imminent hurricane threatens the coastal town of Codeville. 
If at most two people can fit in a rescue boat, 
and the maximum weight limit for a given boat is k, 
determine how many boats will be needed to save everyone.


For example, given a population with weights [100, 200, 150, 80] 
and a boat limit of 200, the smallest number of boats required will be three.

'''


def solution(inp_arr, K):
    inp_arr = sorted(inp_arr)
    boats = 0 
    l = 0 
    r = len(inp_arr) - 1

    while l<=r:
        if inp_arr[l] + inp_arr[r] <= K:
            l+=1
        r-=1
        boats+=1
    return boats


inp_arr = [100, 200, 150, 80]
K = 200

print( solution(inp_arr, K) ) 


inp_arr = [40, 50, 60, 100, 180, 20, 200, 150, 80, 180]
K = 200

print( solution(inp_arr, K) ) 




