
'''
A teacher must divide a class of students into two teams to play dodgeball. 

Unfortunately, not all the kids get along, 
and several refuse to be put on the same team as that of their enemies.

Given an adjacency list of students and their enemies, 
write an algorithm that finds a satisfactory pair of teams, or returns False if none exists.

For example, given the following enemy graph you should return the teams {0, 1, 4, 5} and {2, 3}.
'''

students = {
    0: [3],
    1: [2],
    2: [1, 4],
    3: [0, 4, 5],
    4: [2, 3],
    5: [3]
}

# teams = {0, 1, 4, 5} and {2, 3}. 

students2 = {
    0: [3],
    1: [2],
    2: [1, 3, 4],
    3: [0, 2, 4, 5],
    4: [2, 3],
    5: [3]
}

# teams = False 


# BFS, DFS recursive, DFS iterative 


# 1) BFS 

'''
BFS for a graph is similar to Breadth First Traversal of a tree
However, graphs may contain cycles. 


'''

from collections import defaultdict
 
# adjacency list representation
class Graph:
    def __init__(self):
        # default dictionary to store graph
        self.graph = defaultdict(list)
 
    # function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Function to print a BFS of graph
    def BFS(self, s):
        # Mark all the vertices as not visited
        visited = [False] * (len(self.graph))
        # Create a queue for BFS
        queue = []
        # Mark the source node as
        # visited and enqueue it
        queue.append(s)
        visited[s] = True 
        while queue:
            # Dequeue a vertex from
            # queue and print it
            s = queue.pop(0)
            print (s, end = " ")
            # Get all adjacent vertices of the
            # dequeued vertex s. If a adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

# --- 

g = Graph() 

for elem in students:
    for el in students[elem]:
        print(elem, el)
        g.addEdge(elem, el)


g.BFS(0)