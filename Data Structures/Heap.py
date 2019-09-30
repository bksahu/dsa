"""
This script implements Min-Heaps.
"""

class MinHeap:
    def __init__(self):
        self.items = []

    def leftIndex(self, parent): return 2*parent
    def rightIndex(self, parent): return 2*parent+1
    def parentIndex(self, child): return child//2

    def hasLeft(self, parent): return len(self.items) > 2*parent
    def hasRight(self, parent): return len(self.items) > 2*parent+1
    def hasParent(self, child): return child//2 > -1

    def left(self, parent): return self.items[self.leftIndex(parent)]
    def right(self, parent): return self.items[self.rightIndex(parent)]
    def parent(self, child): return self.items[self.parentIndex(child)]

    def peek(self):
        return self.items[-1]

    def minElement(self):
        return self.items[0]

    @staticmethod
    def swap(indexOne, indexTwo):
        indexOne, indexTwo = indexTwo, indexOne

    def heapifyUp(self):
        index = len(self.items) - 1
        while (self.hasParent(index) and self.parent(index) > self.items[index]):
            self.swap(self.parent(index), self.items[index])
            index = self.parent(index)

    def heapifyDown(self):
        pass

    def add(self, item):
        self.items.append(item)
        self.heapifyUp()

    def poll(self, item):
        if not self.items:
            raise Exception("Heap is empty!")
