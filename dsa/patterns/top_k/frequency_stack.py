"""
Design a class that simulates a Stack data structure, implementing the following two operations:

push(int num): Pushes the number ‘num’ on the stack.
pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.

Example:
After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
1. pop() should return 2, as it is the most frequent number
2. Next pop() should return 1
3. Next pop() should return 2
"""

from heapq import heappush, heappop, heapify

class Element:
    def __init__(self, number, frequency, sequence):
        self.number = number
        self.frequency = frequency
        self.sequence = sequence

    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency > other.frequency
        return self.sequence > other.sequence

class FrequencyStack:
    maxHeap = []
    hashMap = {}
    sequenceNumber = 0

    def push(self, num):
        self.hashMap[num] = self.hashMap.get(num, 0) + 1
        heappush(self.maxHeap, Element(
            num, self.hashMap[num], self.sequenceNumber
        ))
        self.sequenceNumber += 1

    def pop(self):
        num = heappop(self.maxHeap).number
        if self.hashMap[num] > 1:
            self.hashMap[num] -= 1
        else:
            del self.hashMap[num]

        return num

if __name__ == "__main__":
    frequencyStack = FrequencyStack()
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(3)
    frequencyStack.push(2)
    frequencyStack.push(1)
    frequencyStack.push(2)
    frequencyStack.push(5)
    print(frequencyStack.pop())
    print(frequencyStack.pop())
    print(frequencyStack.pop())
