"""
Given an array of ‘K’ sorted LinkedLists, merge them into one sorted list.

Example 1:
Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4]
Output: [1, 2, 3, 3, 4, 6, 6, 7, 8]

Example 2:
Input: L1=[5, 8, 9], L2=[1, 7]
Output: [1, 5, 7, 8, 9]
"""

from heapq import heappush, heappop

class ListNode: 
    def __init__(self, value):
        self.value = value
        self.next = None

    def __lt__(self, other):
        return self.value < other.value

# TC: O(NlogK) where N is the no. of elements & K is the total lists
# SC: O(K) where K is 
def merge_lists(lists):
    minHeap = []
    for head in lists:
        if head: heappush(minHeap, head)

    resultHead = resultTail = None
    while minHeap:
        node = heappop(minHeap)
        if resultHead is None:
            resultHead = resultTail = node
        else:
            resultTail.next = node
            resultTail = resultTail.next

        if node.next is not None:
            heappush(minHeap, node.next)

    return resultHead

if __name__ == "__main__":
    l1 = ListNode(2)
    l1.next = ListNode(6)
    l1.next.next = ListNode(8)

    l2 = ListNode(3)
    l2.next = ListNode(6)
    l2.next.next = ListNode(7)

    l3 = ListNode(1)
    l3.next = ListNode(3)
    l3.next.next = ListNode(4)

    result = merge_lists([l1, l2, l3])
    while result != None:
        print(str(result.value) + " ", end='')
        result = result.next