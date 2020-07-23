"""
Implementation of dijkstra shortest path alogithm with priority queue 
which works only on non-negative DAGs.

Time Complexity: O(ElogV)
"""

from heapq import heappush, heappop
from Dijkstra import DAG

class Dijkstra(DAG):
    def __init__(self):
        super().__init__()

    def dijkstra(self, source):
        pq = []
        heappush(pq, (0, source))
        dist = {node:float("inf") for node in self.graph}
        dist[source] = 0

        while pq:
            _, node = heappop(pq)

            for neighbor in self.graph[node]:
                cost = self.graph[node][neighbor]
                if dist[neighbor] > dist[node] + cost:
                    dist[neighbor] = dist[node] + cost
                    heappush(pq, (dist[neighbor], neighbor))

        print(dist)

if __name__ == "__main__":
    graphList = [
        ("Start", "A", 60),
        ("Start", "B", 2),
        ("A", "Finish", 1),
        ("B", "A", 3),
        ("B", "Finish", 5),
        ("Finish", None, None),
        ]

    g = Dijkstra()
    g.insertFromList(graphList)
    # g.printGraph()
    g.dijkstra("Start")