'''

Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., 
"AA", "AB", ..., "ZZ", "AAA", "AAB", ....

Given a column number, return its alphabetical column id. 

For example, given 1, return "A". Given 27, return "AA".

'''
import math
import string

alp = string.ascii_uppercase

def solution(inp_number):
    base = math.floor( (inp_number / 27) )
    if base>0:
        last_number = inp_number - (base*27)
    else:
        last_number = inp_number - 1
    final = []
    for elem in range(base):
        final.append('A')
    final.append(alp[last_number] )
    final_str = ("").join(final)
    return final_str

inp_number = 1
print( solution(inp_number) )

inp_number = 27
print( solution(inp_number) )


