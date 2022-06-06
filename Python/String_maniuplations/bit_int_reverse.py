'''
This problem was asked by Facebook.

Given a 32-bit integer, return the number with its bits reversed.

For example, given the binary number 

1111 0000 1111 0000 1111 0000 1111 0000, 

return 0000 1111 0000 1111 0000 1111 0000 1111.
'''
# What is really the problem here? 
# Is this just reversing this list? or maybe by 'bits reversed' it means something else?
# Always, clarify your goal and scope
# What format is your input?
#
# If that's just reversing, we can use stack 
# stack - last in, first out 
# 

def solution(bin_number):
    stack = []
    r_number = ''
    for elem in bin_number:
        stack.append(elem)
    while stack:
        r_number = r_number + str(stack.pop())
    return r_number

bin_number = '1111 0000 1111 0000 1111 0000 1111 0000'
print(bin_number)
print(solution(bin_number))

#
# let's assume that input is int and you need to first represent it as bits 
# then revers bits and retern int 
#

def next_sol(num):
    bin_number = '{:032b}'.format(num)
    print(bin_number)
    stack = []
    r_number = ''
    for elem in bin_number:
        stack.append(elem)
    while stack:
        r_number = r_number + str(stack.pop())
    print(r_number)

    return int(r_number, base=2)

num = 4042322160
print(num)
print(next_sol(num))
print("")

num = 252645135
print(num)
print(next_sol(num))
print('')
