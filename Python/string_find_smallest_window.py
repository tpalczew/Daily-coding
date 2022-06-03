
'''
Given a string, find the length of the smallest window 
that contains every distinct character. 
Characters may appear more than once in the window.

For example, given "jiujitsu", 
you should return 5, corresponding to the final five letters.
'''
st = "jiujitsu"

def solver(st):
    '''
    this is our function that will solve this problem 
    Input: string 
    Output: Int, number of letters in the smallest window that 
    contains ever distinct character  
    '''
    # to get every distinct character we can use set
    all_ch = set(st) # O(n) 
    # if we assume that there the window always exists we can just return
    # len of all_ch 
    return len(all_ch) 

print(solver(st))
#--- 

def solver_2(st):
    '''
    let's see how we can do this without using build in function set
    #
    st = "jiujitsu"
    return 5 
    '''
    # we need to keep characters in hash table and use it 
    # to drop duplicates 
    all_ch = [] # I will use just a list
    
    for elem in st: 
        if elem not in all_ch:
            all_ch.append(elem)
    return len(all_ch)
# Again we have O(n) time complexity and we needed to keep hash table so space complexity is also O(n)

print(solver_2(st))

# ---- let's now move to more realistic question 
# what if the window has only part of all distinct characters 
# find the window that is the longest 
'''

"jiujitsuji" -> jiu jitsu ji -> 3 5 2 
return 5 
'''

st = "jiujitsuji"

def solver_3(st):
    counter=0
    max_c = 0 
    all_ch = []
    for elem in st:
        if elem not in all_ch:
            counter+=1
            all_ch.append(elem)
            if counter > max_c:
                max_c = counter
        else:
            counter=1
            all_ch = []
            all_ch.append(elem)
    return max_c 

print(solver_3(st)) 

#------------- Unit-tests / Questions / Constraints 
'''
1) Is input really a string 
2) What if input is empty -> 0 or other indication 
3) A few simple tests ensuring that results are correct 
4) Are there any other constraints? 
'''

def solver_3(st):
    if type(st) == str:
        if len(st) == 0:
            print('Empty string')
            return 0 
        elif len(st) == 1:
            # one or character, the window size is obvious  
            return len(st)
        else:
            counter=0
            max_c = 0 
            all_ch = []
            for elem in st:
                if elem not in all_ch:
                    counter+=1
                    all_ch.append(elem)
                    if counter > max_c:
                        max_c = counter
                else:
                    counter=1
                    all_ch = []
                    all_ch.append(elem)
            return max_c 
    else:
        print('Your input is not a string')
        return -1


def run_test(list_of_tests):
    for index, elem in enumerate(list_of_tests):
        print("Test " + str(index+1))
        print( solver_3(elem) )
        print("Result should be " + str(results[index]))
        print( "")

list_of_tests = [12345, '', 'a', 'abab', 'abacdef', '12abcdef1abca12']
results = [-1, 0, 1, 2, 5, 8]

run_test(list_of_tests)