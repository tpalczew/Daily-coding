'''

Evaluate the value of an arithmetic expression in Reverse Polish Notation. Valid operators are +, -, *, /. Each operand may be an integer or another expression. For example:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6

'''

arr = [2, 1, "+", 3, "*"]


def solution(arr):
    sta = [] 
    for elem in arr:
        if type(elem) is not str:
            sta.append(elem)
            print(sta)
        else:
            a = sta.pop()
            b = sta.pop()
            if elem == "+":
                sta.append( int(a + b) ) 
            elif elem == "*":
                sta.append( int(a * b) )
            elif elem == "-":
                sta.append( int(b - a) )
            elif elem == "/":
                sta.append( int(b / a) )
    return sta 

print( solution(arr) )

arr = [4, 13, 5, "/", "+"]

print( solution(arr) )