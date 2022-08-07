
'''

UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. 
The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.

For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.



'''

def solution(inp_arr):
    
    for index, elem in enumerate(inp_arr):
        bin_rep = format(elem, '#010b')[-8:]

        print(bin_rep)

# we have encoding 
# now we need to add these checks 




inp_arr = [197, 130, 1]

print( solution(inp_arr) )

