'''

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.

So only checking forward, 
ab gives just 0, not 1
'''

print("Sliding Window")

W = 'ab'
S = 'abxaba'

def solution(S, W):
    windowSize = len(W)
    result = []
    for elem in range(len(S)-windowSize+1):
        counter=0
        for el in S[elem:elem+windowSize]:
            if el not in W:
                break
            else:
                counter+=1
        if counter == windowSize:
            result.append(elem)
    return result 

print( solution(S, W) )

'''

 Rabin-Karp algorithm 

1. frequency-based hash of the target word W and check if any window under S hashes to the same value
2. If the hash of the word and window matches, we could do a manual == of the two strings

'''

print("")
print("Rabin Karp Algorithm")


def RabinKarp(S,W,primeNumber):
    result = [] 
    lenS = len(S)
    lenW = len(W)
    AlphabetCharacters = 256 
    hashWord=1
    for i in range(lenW-1):
        hashWord = (AlphabetCharacters * hashWord) % primeNumber
    hashPattern = 0 
    hashText = 0 
    for i in range(lenW):
        # The ord() function returns an integer representing the Unicode character.
        hashPattern = (AlphabetCharacters * hashPattern + ord(W[i])) % primeNumber
        hashText = (AlphabetCharacters * hashText + ord(S[i])) % primeNumber
    for i in range(lenS-lenW+1):
        if hashPattern == hashText:
            for k in range(lenW):
                if S[i + k] != W[k]:
                    break
            k+=1
            if k == lenW:
                result.append(i)
        if i < lenS-lenW:
            hashText = ( AlphabetCharacters * (hashText - ord(S[i]) * hashWord) + ord(S[i+lenW]) ) % primeNumber
            if hashText<0:
                hashText = hashText + primeNumber
    return result 

W = 'ab'
S = 'abxaba'
primeNumber = 101

print ( RabinKarp(S,W,primeNumber) ) 
'''
TO-DO: this just finds a pattern, 
I need to change 
for k in range(lenW):
                if S[i + k] != W[k]:
                    break
to do anagrams 
'''

#---------------------

'''
Frequency Dictionary Approach 
'''

print("")
print("Frequency Dictionary Approach ")

W = 'ab'
S = 'abxaba'

def solution(W, S):
    # make freq dictionary 
    freq = {} 
    result = [] 
    for elem in W:
        if (elem in freq):
            freq[elem] += 1
        else:
            freq[elem] = 1
    #
    for elem in S[:len(W)]:
        if elem in freq:
            freq[elem] -= 1
    if any(freq.values())==0:
        result.append(0)

    for i in range(len(W), len(S)):
        start_elem, end_elem = S[i - len(W)], S[i]
        if start_elem in freq:
            freq[start_elem] += 1
        if end_elem in freq:
            freq[end_elem] -= 1
        
        if any(freq.values())==0:
            beginning_index = i - len(W) + 1
            result.append(beginning_index)
    return result

print ( solution(W,S) ) 