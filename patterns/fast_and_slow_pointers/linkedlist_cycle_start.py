"""
Given the head of a Singly LinkedList that contains a cycle, 
write a function to find the starting node of the cycle.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next
        print()


# def find_cycle_start(head):
#     fast, slow = head, head
    
#     while fast and fast.next:
#         fast = fast.next.next
#         slow = slow.next
#         if fast == slow:
#             break

#     slow = head

#     while True:
#         if fast == slow:
#             return fast
#         fast = fast.next
#         slow = slow.next
  
#     return Node(None) 


def get_cycle_length(head):
    fast, slow = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break

    temp = slow
    cycle_length = 0
    while True:
        cycle_length += 1
        temp = temp.next
        if slow == temp:
            break

    return cycle_length


def find_cycle_start(head):
    length = get_cycle_length(head)
    slow = head
    while length > 0:
        slow = slow.next
        length -= 1

    while slow != head:
        slow = slow.next
        head = head.next

    return head


if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))

    head.next.next.next.next.next.next = head.next.next.next.next.next.next
    print("LinkedList cycle start: " + str(find_cycle_start(head).value))