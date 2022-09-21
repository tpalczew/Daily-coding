'''

Given an input string, reverse the string word by word. A word is defined as a sequence of non-space characters.

The input string does not contain leading or trailing spaces and the words are always separated by a single space.

For example,
Given s = "the sky is blue",
return "blue is sky the".


'''

s = "the sky is blue"

print(s)

def solution(s):
    s = s[::-1]
    final = []
    for elm in s.split(" "):
        final.append( elm[::-1] )
    return ' '.join(final)

print(solution(s))

