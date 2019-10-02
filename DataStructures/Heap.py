"""
This script implements Min-Heaps.
"""

class MinHeap:
    def __init__(self):
        self.items = []

    def leftIndex(self, parent): return 2*parent
    def rightIndex(self, parent): return 2*parent+1
    def parentIndex(self, child): return (child-1)//2

    def hasLeft(self, parent): return len(self.items) > self.leftIndex(parent)
    def hasRight(self, parent): return len(self.items) > self.rightIndex(parent)
    def hasParent(self, child): return self.parentIndex(child) > -1

    def getLeft(self, parent): return self.items[self.leftIndex(parent)]
    def getRight(self, parent): return self.items[self.rightIndex(parent)]
    def getParent(self, child): return self.items[self.parentIndex(child)]

    def peek(self):
        return self.items[-1]

    def minElement(self):
        return self.items[0]

    def printHeap(self):
        return self.items

    def swap(self, indexOne, indexTwo):
        self.items[indexOne], self.items[indexTwo] = self.items[indexTwo], self.items[indexOne]

    def heapifyUp(self):
        index = len(self.items) - 1
        while (self.hasParent(index) and self.getParent(index) > self.items[index]):
            self.swap(self.parentIndex(index), index)
            index = self.parentIndex(index)

    def heapifyDown(self):
        index = 0
        while (self.hasLeft(index)):
            if (self.hasRight(index) and self.getRight(index) < self.getLeft(index)):
                smallestChildIndex = self.rightIndex(index)
            else:
                smallestChildIndex = self.leftIndex(index)

            if self.items[index] < self.items[smallestChildIndex]:
                break
            else:
                self.swap(index, smallestChildIndex)

            index = smallestChildIndex


    def add(self, item):
        self.items.append(item)
        self.heapifyUp()

    def poll(self):
        if not self.items:
            raise Exception("Heap is empty!")
        self.items[0] = self.items.pop()
        self.heapifyDown()


if __name__ == "__main__":
    heap = MinHeap()
    heap.add(10)        
    heap.add(15)        
    heap.add(20)        
    heap.add(17)        
    print(heap.printHeap())
    heap.add(8)
    print(heap.printHeap())
    heap.poll()
    print(heap.printHeap())