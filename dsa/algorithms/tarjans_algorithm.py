"""
Used to find strongly connected components (SCC) in a Graph.

TC: O(V+E)
SP: O(V)
"""

from collections import defaultdict


def findSccs(n, edges):
    g = defaultdict(list)  # graph

    for u, v in edges:
        g[u] += v,

    UNVISITED = -1

    id = 0  # used to give each node an id
    sccCount = 0  # used to count number of SCCs found
    ids = [UNVISITED]*n  # ids of the nodes
    low = [0]*n  # lowLinks of the nodes
    onStack = [False]*n  # tracks nodes which are ont stack currently
    stack = []  # stack to track our processing nodes

    def dfs(at):
        nonlocal id, sccCount
        stack.append(at)
        onStack[at] = True
        ids[at] = low[at] = id
        id += 1

        # visit all neighbours and min low-link on callback
        for to in g[at]:
            if (ids[to] == UNVISITED):
                dfs(to)
            if onStack[to]:
                low[at] = min(low[at], low[to])

        # After having visited all the neighbours of 'at'
        # if we're at the start of the SCC empty the seen
        # stack until we are back at the start of SCC
        if ids[at] == low[at]:
            while stack:
                node = stack.pop()
                onStack[node] = False
                low[node] = ids[at]
                if node == at:
                    break
            sccCount += 1

    for i in range(n):
        if ids[i] == UNVISITED:
            dfs(i)
    print(sccCount)
    return low


def findSccsUnDirected(n, edges):
    """
    Idea is to find loops and set the lowLink value
    for the current node the minimum of it's neightbour's 
    lowLink value exculuding it's parent (since it is a 
    undirected graph)
    """
    graph = defaultdict(list)  # graph

    for u, v in edges:
        graph[u] += v,
        graph[v] += u,

    levels = [None]*n # levels/ids/ranks of the nodes
    lowLinks = [None]*n # low-links of the nodes

    def dfs(node, parent, currLevel):
        if levels[node] is not None: # it is already visited
            return
        
        levels[node] = lowLinks[node] = currLevel
        for neighbour in graph[node]:
            if levels[neighbour] is None: # not yet visited
                dfs(neighbour, node, currLevel+1) # set the parent as the current node
        
        # set the lowLink of current node as the minimum of
        # the lowLink values of it's neightbours excluding it's
        # parent
        lowLinks[node] = min([currLevel] + [lowLinks[neighbour] for neighbour in graph[node] if neighbour != parent]) 

    # start from 0th node with level set as 0
    dfs(0, None, 0)

    return lowLinks

if __name__ == "__main__":
    print(findSccs(
        8,
        [[3, 7], [7, 3], [3, 4], [7, 5], [4, 5], [5, 0], [
            5, 6], [6, 4], [6, 0], [0, 1], [1, 2], [2, 0], [6, 2]]
    ))
    print(findSccsUnDirected(
        5,
        [[1, 0], [2, 0], [3, 2], [4, 2], [4, 3], [3, 0], [4, 0]]
    ))
