'''

You come across a dictionary of sorted words in a language you've never seen before. 
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y'].

xww

wxyz

wxyw

ywx

ywz

-> x, z, w, y 

This one is hard. Maybe graph and topological sort. 
'''

from collections import defaultdict
 
#Class to represent a graph
class Graph:
    def __init__(self,vertices):
        self.graph = defaultdict(list) # dictionary containing adjacency list
        self.V = vertices # number of vertices
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
    # a recursive function
    def topologicalSortUtil(self,v,visited,stack):
        # node as visited
        visited[v] = True
        # recur all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
        # push current vertex to stack
        stack.insert(0,v)
    # topological sort
    def topologicalSort(self):
        # not visited
        visited = [False]*self.V
        stack =[]
        # sort
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i,visited,stack)
        # return stack
        return stack

def solution(example):
    str_ex = ''.join(example)
    set_ex = list(set(str_ex)) # number of verticies 
    g= Graph( int( len(set_ex) ) ) # graph
    print(g.V)
    print(set_ex)
    map_l = {}
    map_l_r = {}
    for index, elem in enumerate(set_ex):
        map_l[elem] = index  
        map_l_r[index] = elem
    print(map_l)
    print("")
    print(map_l_r)
    for index in range(len(str_ex)-1):
        if str_ex[index] != str_ex[index+1]:
            print( str_ex[index], str_ex[index+1] )
            print( map_l[str_ex[index]], map_l[str_ex[index+1]] )
            g.addEdge( map_l[str_ex[index]], map_l[str_ex[index+1]] )
    vs = g.topologicalSort()
    print(vs)
    results = []
    for ind in vs: 
        results.append(map_l_r[ind])
    return results

example = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
print(example)

print(solution(example))

# For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'], you should return ['x', 'z', 'w', 'y']. 

'''
Graph is not created correctly, 
the edges should be between mismatching characters in adjusted words

xww
wxyz

x->w

I need to think about this, will come back later to this problem
'''