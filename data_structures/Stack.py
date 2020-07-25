# -*- coding: utf-8 -*-

""" This script implements Stacks.
"""

from __future__ import print_function

class Stack:
    """ Class implementing stack """
    def __init__(self):
        """ Empty list to store elements. """
        self.container = []
        self.top = None

    def isEmpty(self):
        """ Return True if stack is empty. """
        return False if self.container else True

    def push(self, element):
        """ Append element to the top and
        update top.
        """
        if self.isEmpty():
            self.container.append(element)
        else:
            self.container.insert(0, element)

        self.top = element

    def pop(self):
        """ Delete the Top and return it
        """
        if not self.isEmpty():
            popped_element = self.container[0]
            del self.container[0]
            self.top = self.container[0] if self.container else None
            return popped_element
        else:
            return None

    def getTop(self):
        """ Return the Top """
        return self.top

    def getLength(self):
        """ Return Stack length """
        return len(self.container)

    def show(self):
        """ Display the Stack """
        if self.isEmpty():
            print("Stack is empty")
        else:
            print("Top -> ", end="")
            for element in self.container:
                print("{0} ".format(element), end='')
            print("")


if __name__ == "__main__":
    stack = Stack()
    print(stack.isEmpty())
    print(stack.push(3))
    print(stack.push(4))
    print(stack.show())
    print(stack.isEmpty())
    print(stack.pop())
    print(stack.getLength())
    print(stack.getTop())
    print(stack.pop())
    print(stack.isEmpty())
    print(stack.show())