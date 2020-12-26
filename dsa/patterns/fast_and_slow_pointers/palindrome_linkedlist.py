'''
Given the head of a Singly LinkedList, write a method to check if the LinkedList
 is a palindrome or not.

Your algorithm should use constant space and the input LinkedList should be in the original
 form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where
  ‘N’ is the number of nodes in the LinkedList.

Example 1:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
Output: true

Example 2:
Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
Output: false
'''
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev
        


def is_palindromic_linked_list(head):
    slow, fast = head, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    slow = reverse(slow)
    temp = slow

    while slow and head:
        if slow.value != head.value:
            break
        slow = slow.next
        head = head.next

    reverse(temp)


    return True if not slow or not head else False    

    

if __name__ == "__main__":
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(6)
    head.next.next.next.next = Node(4)
    head.next.next.next.next.next = Node(2)

    print("Is palindrome: " + str(is_palindromic_linked_list(head)))


    head.next.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(is_palindromic_linked_list(head)))