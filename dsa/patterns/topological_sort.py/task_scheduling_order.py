"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be 
completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a 
method to find the ordering of tasks we should pick to finish all tasks.

Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: To execute task '1', task '0' needs to finish first. Similarly, task '1' needs to finish 
before '2' can be scheduled. A possible scheduling of tasks is: [0, 1, 2] 

Example 2:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2], [2, 0]
Output: []
Explanation: The tasks have cyclic dependency, therefore they cannot be scheduled.

Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: [0 1 4 3 2 5] 
Explanation: A possible scheduling of tasks is: [0 1 4 3 2 5] 
"""

from collections import deque

# BFS
# def find_order(tasks, preprequisites):
#     sortedOrder = []
#     if tasks <= 0:
#         return sortedOrder

#     inDegree = {i:0 for i in range(tasks)}
#     graph = {i:[] for i in range(tasks)}

#     for vertex, edge in preprequisites:
#         graph[vertex] += edge,
#         inDegree[edge] += 1

#     source = deque([vertex for vertex, edge in inDegree.items() if edge == 0])
    
#     while source:
#         node = source.popleft()
#         sortedOrder += node,

#         for child in graph[node]:
#             inDegree[child] -= 1
#             if inDegree[child] == 0:
#                 source += child,

#     return sortedOrder if len(sortedOrder) == tasks else []


# DFS
def find_order(tasks, preprequisites):
    graph = {i: [] for i in  range(tasks)}
    visited = [0]*tasks
    stack = []

    for vertex, edge in preprequisites:
        graph[vertex] += edge,

    def dfs(node):
        nonlocal visited
        nonlocal stack

        if visited[node] == -1: # cycle detected
            return False

        if visited[node] == 1: # already processed
            return True

        visited[node] = -1 # procssing

        for child in graph[node]:
            if not dfs(child):
                return False
        
        visited[node] = 1 # processed
        stack += node,
        return True 

    for i in range(tasks):
        if not dfs(i):
            return []

    return stack[::-1]

if __name__ == "__main__":
    print(find_order(3, [[0,1], [2,1]]))
    print(find_order(3, [[0,1], [1,2]]))
    print(find_order(3, [[0,1], [1,2], [2,0]]))
    print(find_order(6, [[2,5], [0,5], [0,4], [1,4], [3,2], [1,3]]))