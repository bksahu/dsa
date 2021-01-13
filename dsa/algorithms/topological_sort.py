"""
This following script implements Topological Sorting Algorithm using DFS, that works
only on Directed Acyclic Graphs.

COLOUR CODES
============
0: YET TO BE PROCESSED
1: PROCESSED SUCESSFULLY
-1: PROCESSING 

If we get -1 in between, then we can be sure that we got a cycle in the graph

TC: Since each vertex will become source only once and each edge will be added and 
removed only once. So, Time Complexity will be O(V + E)

SC: The space complexity will be O(V+E)O(V+E), since we are storing all of the edges
for each vertex in an adjacency list.
"""


from collections import defaultdict 
    
class Graph: 
    def __init__(self, vertices): 
        self.graph = defaultdict(list)  # dictionary containing adjacency List 
        self.V = vertices  # No. of vertices 
  
    # function to add an edge to graph 
    def addEdge(self, u, v): 
        self.graph[u].append(v) 

    # function to topological sort
    def topologicalSort(self):
        self.visited = [0]*self.V
        self.stack = []

        for i in range(self.V):
            if not self.dfs(i):
                raise ValueError("Cycle detected")
            
        print(self.stack[::-1])

    # dfs to visit all the unvisited nodes
    def dfs(self, i):
        if self.visited[i] == -1: # cycle dected
            return False

        if self.visited[i] == 1: # already processed
            return True

        self.visited[i] = -1 # processing

        for node in self.graph[i]:
            if not self.dfs(node):
                return False

        self.visited[i] = 1 # processed
        self.stack += i,
        return True

if __name__ == "__main__":
    g = Graph(6) 
    g.addEdge(5, 2) 
    g.addEdge(5, 0) 
    g.addEdge(4, 0) 
    g.addEdge(4, 1) 
    g.addEdge(2, 3) 
    g.addEdge(3, 1) 
  
    g.topologicalSort() 

    # With Cycle
    g = Graph(6) 
    g.addEdge(5, 2) 
    g.addEdge(5, 0) 
    g.addEdge(4, 0) 
    g.addEdge(0, 5) 
    g.addEdge(2, 3) 
    g.addEdge(3, 1) 
  
    try:
        g.topologicalSort() 
    except ValueError as error:
        print(error)
        