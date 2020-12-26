"""
Implementation of dijkstra shortest path alogithm which works
only on non-negative DAGs.

Time Complexity: O(|V|^2)

"""
class DAG:
    def __init__(self):
        self.graph = {}

    def insert(self, fromNode, toNode, cost):
        """
        Create a dict containg {vertex: {neighbor:cost}}
        """
        if fromNode not in self.graph:
            self.graph[fromNode] = {}
        if toNode:
           self.graph[fromNode][toNode] = cost 

    def printGraph(self):
        """
        Print the graph
        """
        print(self.graph)

    def insertFromList(self, graphList):
        """
        List: [(fromNode, toNode, cost),...]
        """
        for fromNode, toNode, cost in graphList:
            self.insert(fromNode, toNode, cost)

    def buildCostsAndParentsTable(self, start):
        """
        Builds Costs table and Parents table
        """
        costs, parents = {}, {}
        for node in self.graph:
            if node != start:
                costs[node] = self.graph[start].get(node, float("inf"))
                parents[node] = None

        for child in self.graph[start]:
            parents[child] = start

        return costs, parents

    def getPath(self, parents, start, end):
        currNode = end
        path = ""

        while currNode != start:
            path = "->" + currNode + path
            currNode = parents[currNode]
        return start + path

    def getLowestCostNode(self, costs, processed):
        lowestCostNode = None
        lowestCost = float("inf")
        for node in costs:
            if costs[node] < lowestCost and node not in processed:
                lowestCost = costs[node]
                lowestCostNode = node
        return lowestCostNode

    def dijkstra(self, start, end):
        """
        Run dijkstra algorithm to find the shortest path
        """
        costs, parents = self.buildCostsAndParentsTable(start)
        processed = []

        node = self.getLowestCostNode(costs, processed)

        while node:
            cost = costs[node]
            neighbors = self.graph[node]
            for n in neighbors.keys():
                newCost = cost + neighbors[n]
                if costs[n] > newCost:
                    costs[n] = newCost
                    parents[n] = node
            processed.append(node)
            node = self.getLowestCostNode(costs, processed)

        return costs[end], self.getPath(parents, start, end)

if __name__ == "__main__":
    graphList = [
        ("Start", "A", 6),
        ("Start", "B", 2),
        ("A", "Finish", 1),
        ("B", "A", 3),
        ("B", "Finish", 5),
        ("Finish", None, None),
        ]

    g = DAG()
    g.insertFromList(graphList)
    # g.printGraph()
    cost, shortestPath = g.dijkstra("Start", "Finish")
    print(f"Path: {shortestPath}\nCost: {cost}")