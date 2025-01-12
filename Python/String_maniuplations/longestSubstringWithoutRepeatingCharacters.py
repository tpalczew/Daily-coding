'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''


# sliding window approach 

def solution(s):
	c = []
	left = 0
	max_len = 0 
	# 	
	for right in range(len(s)):
		while s[right] in c:
			c.remove(s[left])
			left += 1
		c.append(s[right])
		max_len = max(max_len, right-left+1)
	return max_len 

'''

abcabcbb

1st)
r = 0 -> s[0] = a; a not in c -> c = [a], max_len = 1; l = 0 
2nd) 
r = 1 -> s[1] = b; b not in c -> c = [a, b], max_len = 2, l = 0 
3rd)
r = 2 -> s[2] = c, c not in c -> c = [a,b,c], max_len = 3, l = 0 
4th)
r = 3 -> s[3] = a, a in c -> c = [b, c], max_len = 3, l = 1 
5th)
r = 4 -> s[4] = b, b in c -> c = [c], max_len = 3, l = 2 
6th) 
r = 5 -> s[5] = c, c in c -> c = [], max_len = 3, l = 3 
7th) 
r = 6 -> s[6] = b, b not in -> c = [b], max_len = 3, l = 3
...

'''



s = "abcabcbb"
print(solution(s))


s = "bbbbb"
print(solution(s))

s = "pwwkew"
print(solution(s))


s = "abcabcbbmngtyhiujklbsedaaaaaa"
print(solution(s))


 
		
				


