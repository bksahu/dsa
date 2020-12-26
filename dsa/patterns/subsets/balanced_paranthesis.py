"""
For a given number ‘N’, write a function to generate all combination of ‘N’ pairs of balanced parentheses.

Example 1:
Input: N=2
Output: (()), ()()

Example 2:
Input: N=3
Output: ((())), (()()), (())(), ()(()), ()()()
"""

from collections import deque

class ParenthesesString:
    def __init__(self, s, openCount, closeCount):
        self.s = s
        self.openCount = openCount
        self.closeCount = closeCount


def generate_valid_parentheses(num):
    result = []
    queue = deque()
    queue.append(ParenthesesString("", 0, 0))

    while queue:
        ps = queue.popleft()
        if ps.openCount == num and ps.closeCount == num:
            result.append(ps.s)
        else:
            if ps.openCount < num:
                queue.append(
                    ParenthesesString(
                        ps.s + '(', ps.openCount+1, ps.closeCount
                    )
                )
            
            if ps.closeCount < ps.openCount:
                queue.append(
                    ParenthesesString(
                        ps.s + ')', ps.openCount, ps.closeCount+1
                    )
                )


    return result

if __name__ == "__main__":
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(2)))
    print("All combinations of balanced parentheses are: " +
        str(generate_valid_parentheses(3)))
