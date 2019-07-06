# -*- coding: utf-8 -*-

""" This script implements Singly Linked List.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head=None):
        self.head = Node(head)

    def isEmpty(self):
        return False if self.head.value else True

    def insertAtEnd(self, value):
        curr = self.head
        if self.isEmpty():
            curr.value = value
        else:
            while curr.next:
                curr = curr.next
            curr.next = Node(value)

    def insertAtHead(self, value):
        curr = self.head
        if self.isEmpty():
            curr.value = value
        else:
            new_head = Node(value)
            new_head.next = curr
            self.head = new_head

    def delete(self, value):
        curr = self.head
        deleted = False
        if self.isEmpty():
            return None
        else:
            if curr.value == value:
                self.head = curr.next
                deleted = True
            else:
                while curr.next != None:
                    if curr.next.value == value:
                        deleted = True
                        curr.next = curr.next.next
                        break
                    curr = curr.next
        if not deleted:
            print("Element Not found")

    def reverseItr(self):
        """Reverse using iteration"""
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def reverseRec(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return

        next = curr.next
        curr.next = prev
        prev = curr
        self.reverseRec(next, prev)

    def reverse(self):
        if self.head is None:
            return None
        return self.reverseRec(self.head, None)

    def show(self):
        curr = self.head
        if not curr:
            print("Linked List is empty.")
        else:
            print("HEAD -> ", end="")
            while curr:
                print("{0} ".format(curr.value), end="")
                curr = curr.next
            print("")


if __name__ == "__main__":
    ll = LinkedList()
    # ll.insertAtEnd(1)
    # ll.insertAtEnd(2)
    ll.insertAtEnd(3)
    ll.insertAtEnd(4)
    # ll.show()
    ll.insertAtHead(1)
    ll.insertAtHead(2)
    # ll.insertAtHead(3)
    # ll.insertAtHead(4)
    # ll.show()
    # ll.delete(2)
    # ll.show()
    # ll.delete(11)
    ll.show()
    # ll.delete(1)
    # ll.show()
    # ll.delete(4)
    # ll.show()
    ll.reverse()
    ll.show()