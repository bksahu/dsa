"""
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have some prerequisite tasks which need to be 
completed before it can be scheduled. Given the number of tasks and a list of prerequisite pairs, write a 
method to print all possible ordering of tasks meeting all prerequisites.

Example 1:
Input: Tasks=3, Prerequisites=[0, 1], [1, 2]
Output: [0, 1, 2]
Explanation: There is only possible ordering of the tasks.

Example 2:
Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.

Example 3:
Input: Tasks=6, Prerequisites=[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]
Output: 
1) [0, 1, 4, 3, 2, 5]
2) [0, 1, 3, 4, 2, 5]
3) [0, 1, 3, 2, 4, 5]
4) [0, 1, 3, 2, 5, 4]
5) [1, 0, 3, 4, 2, 5]
6) [1, 0, 3, 2, 4, 5]
7) [1, 0, 3, 2, 5, 4]
8) [1, 0, 4, 3, 2, 5]
9) [1, 3, 0, 2, 4, 5]
10) [1, 3, 0, 2, 5, 4]
11) [1, 3, 0, 4, 2, 5]
12) [1, 3, 2, 0, 5, 4]
13) [1, 3, 2, 0, 4, 5]
"""

from collections import deque

def print_orders(tasks, preprequisites):
    if tasks <= 0: return []
    inDegree = {i:0 for i in range(tasks)}
    graph = {i:[] for i in range(tasks)}

    for u, v in preprequisites:
        graph[u] += v,
        inDegree[v] += 1

    sources = deque([v for v, _ in graph.items() if inDegree[v] == 0])
    print_all_tasks(inDegree, graph, sources, [])

def print_all_tasks(inDegree, graph, sources, sortedOrder):
    if sources:
        for vertex in sources:
            sortedOrder.append(vertex)
            sourcesForNextCall = deque(sources)

            sourcesForNextCall.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] -= 1
                if inDegree[child] == 0:
                    sourcesForNextCall.append(child)

            print_all_tasks(inDegree, graph, sourcesForNextCall, sortedOrder)

            sortedOrder.remove(vertex)
            for child in graph[vertex]:
                inDegree[child] += 1

    if len(sortedOrder) == len(inDegree):
        print(sortedOrder)

if __name__ == "__main__":
    print("Task Order: ")
    print_orders(3, [[0, 1], [1, 2]])
    print("Task Order: ")
    print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
    print("Task Order: ")
    print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])