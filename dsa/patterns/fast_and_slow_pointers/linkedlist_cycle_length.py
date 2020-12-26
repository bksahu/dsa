"""
Given the head of a LinkedList with a cycle, find the length of the cycle.
"""

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

def has_cycle(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

def cycle_length1(head):
    if not has_cycle(head):
        return 0

    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    
    fast = head # reset fast

    while fast != slow:
        fast = fast.next.next
        slow = slow.next

    cycle_entry_node = fast.next
    cycle_length = 1

    while cycle_entry_node != slow:
        cycle_length += 1
        cycle_entry_node = cycle_entry_node.next

    return cycle_length

def cycle_length(head):
    fast, slow = head, head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

        if fast == slow:
            return calculate_cycle_length(slow)

    return 0

def calculate_cycle_length(slow):
    temp = slow
    cycle_length = 0

    while True:
        temp = temp.next
        cycle_length += 1
        if temp == slow:
            break

    return cycle_length


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    print("Cycle length: " + str(cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next
    print("Cycle length: " + str(cycle_length(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("Cycle length: " + str(cycle_length(head)))
