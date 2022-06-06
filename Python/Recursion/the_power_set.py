'''
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.

You may also use a list or array to represent a set.
'''

'''
let's do a few examples 

{1,2} ->        {{}, {1}, {2},           {1,2}}
{1, 2, 3} ->    {{}, {1}, {2}, {3},      {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}
{1, 2, 3, 4} -> {{}, {1}, {2}, {3}, {4}, {1, 2}, {1, 3}, {1, 4}, {2, 3}, {2, 4}, {1, 2, 3}, ... 

'''

def solution(string , index , subs):
     
    #print('index ', index)
    #print('string ', string)
    #print('subs ', subs)

    if index == len(string):
        print(subs)
        return
     
    solution(string, index + 1, subs + string[index])
    solution(string, index + 1, subs)
     

s1 = "12345"
index = 0
subs = ""
solution(s1, index , subs)






