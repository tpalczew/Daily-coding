'''

Given an absolute pathname that may have 

. or .. as part of it, return the shortest standardized path.

For example, given 

"/usr/bin/../bin/./scripts/../", 

return "/usr/bin/".

'''

def solution(inp_str):
    '''
    input: str of path
    out: std path
    '''
    elements = inp_str.split("/")
    std_path = []
    for elem in elements:
        if elem == "..":
            if len(std_path)>1:
                std_path.pop()
        elif elem != ".":
            std_path.append(elem)
    return "/".join(std_path)

inp_str = "/usr/bin/../bin/./scripts/../"
print( solution(inp_str))

inp_str = "/usr/bin/../local/files/./scripts/../"
print( solution(inp_str))

inp_str = "/usr/bin/../local/files/./scripts/"
print( solution(inp_str))

inp_str = "/usr/bin/../local/files/./scripts/../../../"
print( solution(inp_str))