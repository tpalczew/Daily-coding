'''

Given a string of round, curly, and square open and closing brackets, 
return whether the brackets are balanced (well-formed).

For example, given the string "([])[]({})", you should return true.

Given the string "([)]" or "((()", you should return false.

'''


def balance(inp_str):
    s = []
    for elem in inp_str:
        s.append(elem)
        if elem == ']':
            if s[-2] == '[':
                s.pop()
                s.pop()
            else:
                return False
        if elem == ')':
            if s[-2] == '(':
                s.pop()
                s.pop()
            else:
                return False
        if elem == '}':
            if s[-2] == '{':
                s.pop()
                s.pop()
            else:
                return False
    if s:
        return False
    else:
        return True

inp_str = "([])[]({})"

print( balance(inp_str) )

inp_str = "([)]" 

print( balance(inp_str) )

inp_str =  "((()"

print( balance(inp_str) )

inp_str = "(())[[()]]({([])})"

print( balance(inp_str) )


def balance2(inp_str):
    s = []
    for elem in inp_str:
        if elem in ["(", "[", "{"]:
            s.append(elem)
        else:
            if elem == ")":
                if s[-1] == "(":
                    s.pop()
                else:
                    return False
            if elem == "]":
                if s[-1] == "[":
                    s.pop()
                else:
                    return False
            if elem == "}":
                if s[-1] == "{":
                    s.pop()
                else:
                    return False
    if s:
        return False
    else:
        return True

print("--------- second --------- ")

inp_str = "([])[]({})"

print( balance2(inp_str) )

inp_str = "([)]" 

print( balance2(inp_str) )

inp_str =  "((()"

print( balance2(inp_str) )

inp_str = "(())[[()]]({([])})"

print( balance2(inp_str) )

 
