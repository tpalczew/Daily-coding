'''
Suppose we represent our file system by a string in the following manner:

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

dir
    subdir1
    subdir2
        file.ext
The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

The string "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext" represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext
The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext 
and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 
containing a file file2.ext.

We are interested in finding the longest (number of characters) absolute path 
to a file within our file system. For example, in the second example above, 
the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", 
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, 
return the length of the longest absolute path to a file in the abstracted file system. 
If there is no file in the system, return 0.

Note:

The name of a file contains at least a period and an extension.

The name of a directory or sub-directory will not contain a period.


-> you can use period to identify files 

'''

# --- 1 - string manipulation 
'''
dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext


dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

'''

input_st = 'dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext'

arr = input_st.split("\n")

print(arr)

# ['dir', '\tsubdir1', '\t\tfile1.ext', '\t\tsubsubdir1', '\tsubdir2', '\t\tsubsubdir2', '\t\t\tfile2.ext']

'''
dir 
    subdir 
        file1
        subsubdir1
    subdir2
        subsubdir2
            file2.ext 

\t tells you depth
'''


def solution(input_str):
    arr = input_str.split("\n")
    stack = []
    path = []
    all_paths = []
    maxlen = 0
    #
    for elem in arr:
        print(elem)
        w = elem.lstrip("\t")
        print(w)
        depth = len(elem) - len(w)
        print(depth)
        while stack and stack[-1] >= depth:
                stack.pop()
                path.pop()
        stack.append(depth)
        path.append(w)
        if '.' in w:
            all_paths.append('/'.join(path))
    maxlen = max([len(path) for path in all_paths])
    return maxlen


input_str_test = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

#input_str_test = "dir\n\tsubdir1\n\t\tfile1.ext"

print(solution(input_str_test))

'''
21
file1.ext
38
file2.ext


dir\n\tsubdir1\n\t\tfile1.ext

dir                             0
    subdir                      1
        file11.ext              2   

3 + 7 + 9 = 19 
dir + subdir1 + file1.ext
19 + depth (2) = 21 

dir\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext

dir                             0
    subdir2                     1
        subsubdir2              2
            file2.ext           3

3 + 7 + 10 + 9 = 29 

29 + depth (3) = 32
'''






