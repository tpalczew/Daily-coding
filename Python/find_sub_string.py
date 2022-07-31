'''

Given a string s and a list of words words, 
where each word is the same length, 
find all starting indices of substrings in s that 
is a concatenation of every word in words exactly once.

For example, given s = "dogcatcatcodecatdog" and words = ["cat", "dog"], 
return [0, 13], since "dogcat" starts at index 0 and "catdog" starts at index 13.

Given s = "barfoobazbitbyte" and words = ["dog", "cat"], return [] 
since there are no substrings composed of "dog" and "cat" in s.

The order of the indices does not matter.
'''


inp_str = "dogcatcatcodecatdog"
words = ["cat", "dog"]


from itertools import permutations

def get_indices(s, words):
    perms = list(permutations(words))
    perms = [x + y for (x, y) in perms]
    indices = [s.find(x) for x in perms]
    indices = [x for x in indices if x >= 0]
    return sorted(indices)

inp_str = "dogcatcatcodecatdog"
words = ["cat", "dog"]

print( get_indices(inp_str, words) )

inp_str = "barfoobazbitbyte"
words = ["dog", "cat"]

print( get_indices(inp_str, words) )