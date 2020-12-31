"""
Given an array of points in the a 2D plane, find ‘K’ closest points to the origin.

Example 1:
Input: points = [[1,2],[1,3]], K = 1
Output: [[1,2]]
Explanation: The Euclidean distance between (1, 2) and the origin is sqrt(5).
The Euclidean distance between (1, 3) and the origin is sqrt(10).
Since sqrt(5) < sqrt(10), therefore (1, 2) is closer to the origin.

Example 2:
Input: point = [[1, 3], [3, 4], [2, -1]], K = 2
Output: [[1, 3], [2, -1]]
"""

from heapq import heappush, heappop

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def print_point(self):
        print("[" + str(self.x) + "," + str(self.y) + "]")

def distance(p1, p2):
    return (p1.x - p2.x)**2 + (p1.y - p2.y)**2

def find_closest_point(points, k):
    heap = []
    origin = Point(0, 0)

    for i in range(k):
        heappush(heap, [-distance(points[i], origin), points[i]])

    for i in range(k, len(points)):
        d = distance(points[i], origin)
        if d < -heap[0][0]:
            heappop(heap)
            heappush(heap, [-d, points[i]]) 

    return [point for _, point in heap]

if __name__ == "__main__":
    points = find_closest_point([Point(1,2), Point(1,3)], 1)
    for point in points:
        point.print_point()
    print()
    points = find_closest_point([Point(1,3), Point(3,4), Point(2,-1)], 2)
    for point in points:
        point.print_point()