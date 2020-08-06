"""
Given an array of characters where each character represents a fruit tree, 
you are given two baskets and your goal is to put maximum number of fruits 
in each basket. The only restriction is that each basket can have only one 
type of fruit.

You can start with any tree, but once you have started you can’t skip a tree. 
You will pick one fruit from each tree until you cannot, i.e., you will stop 
when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Example 2:
Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
"""

from collections import defaultdict

def solution(fruits):
    winStart, maxFruits = 0, 0
    fruitsFreq = defaultdict(int)

    for winEnd in range(len(fruits)):
        winEndFruit = fruits[winEnd]
        fruitsFreq[winEndFruit] += 1

        if len(fruitsFreq) > 2:
            winStartFruit = fruits[winStart]
            fruitsFreq[winStartFruit] -= 1
            if fruitsFreq[winStartFruit] == 0:
                fruitsFreq.pop(winStartFruit)
            winStart += 1

        maxFruits = max(maxFruits, winEnd - winStart + 1)

    return maxFruits

if __name__ == "__main__":
    print(solution(['A', 'B', 'C', 'A', 'C']))
    print(solution(['A', 'B', 'C', 'B', 'B', 'C']))