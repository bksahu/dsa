# -*- coding: utf-8 -*-

""" This script implements unweighted Graphs.
"""

class Graph:
    def __init__(self, vertices=None):
        """ initializes the graph object """
        if vertices:
            self._graph = vertices
        else:
            self._graph = {}

    def getVertices(self):
        return self._graph.keys()

    def getEdges(self):
        return self._generate_edges()

    def _generate_edges(self):
        """ generate all the edges and return
        a list of (from_node, to_node)
        """
        edges = []
        for from_node in self._graph:
            for to_node in self._graph[from_node]:
                if to_node:
                    edges.append((from_node, to_node))

        return edges

    def addVertices(self, from_node, to_node):
        self._graph[from_node] = to_node

    def printGraph(self):
        # TODO: Consider using graphviz
        pass

    def getPaths(self, start, end, path=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in self._graph.keys():
            return []
        paths = []
        for node in self._graph[start]:
            if node not in path:
                newPaths = self.getPaths(node, end, path)
                for newPath in newPaths:
                    paths.append(newPath)
        return paths

    def getIndex(self, element):
        return list(self._graph.keys()).index(element)

    def DFSUtil(self, s, visited):
        print(s, end=" ")

        visited[self.getIndex(s)] = True

        for i in self._graph[s]:
            if not visited[self.getIndex(i)]:
                self.DFSUtil(i, visited)

    def DFS(self, start):
        visited = [False] * len(self._graph)

        self.DFSUtil(start, visited)        

    def BFS(self, start):
        visited = [False] * len(self._graph)

        # Queue for BFS
        queue = []

        queue.append(start)
        visited[self.getIndex(start)] = True

        while queue:
            s = queue.pop(0)
            print (s, end=" ")

            for i in self._graph[s]:
                idx = self.getIndex(i)
                if visited[idx] == False:
                    queue.append(i)
                    visited[idx] = True


if __name__ == "__main__":
    # g = Graph({'A': ['B', 'C'],
    #            'B': ['C', 'D'],
    #            'C': ['D'],
    #            'D': ['E'],
    #            'E': [],
    #     })
    # g.addVertices("E", ["D"])
    # print(g.getEdges())
    # print(g.getPaths("A", "D"))
    g = Graph({0: [1, 2], 1: [2], 2: [0, 3], 3: [3]})
    g.DFS(2)