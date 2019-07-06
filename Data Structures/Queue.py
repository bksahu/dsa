# -*- coding: utf-8 -*-

""" This script implements Queue.
"""

class Queue:
    def __init__(self):
        self.queue = []
        self.front = None
        self.back = None

    def isEmpty(self):
        return False if self.queue else True

    def getTop(self):
        return None if self.isEmpty() else self.queue[0]

    def enqueue(self, element):
        return self.queue.append(element)

    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            dequeued_element = self.queue[-1]
            del self.queue[-1]
            return dequeued_element

    def show(self):
        if self.isEmpty():
            print("Queue is Empty")
        else:
            print("Front -> |", end="")
            for element in self.queue:
                print("{0}|".format(element), end="")
            print(" <- Back")

if __name__ == "__main__":
    q = Queue()
    q.enqueue(3)
    q.enqueue(4)
    q.show()
    q.dequeue()
    q.show()