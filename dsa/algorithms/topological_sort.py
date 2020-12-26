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
        self.visited = [False]*self.V
        self.stack = []

        for i in range(self.V):
            if not self.visited[i]:
                self.dfs(i)
            
        print(self.stack[::-1])

    # dfs to visit all the unvisited nodes
    def dfs(self, i):
        self.visited[i] = True

        for node in self.graph[i]:
            if not self.visited[node]:
                self.dfs(node)

        self.stack += i,

if __name__ == "__main__":
    g = Graph(6) 
    g.addEdge(5, 2) 
    g.addEdge(5, 0) 
    g.addEdge(4, 0) 
    g.addEdge(4, 1) 
    g.addEdge(2, 3) 
    g.addEdge(3, 1) 
  
    g.topologicalSort() 