"""
You are given a list of tasks that need to be run, in any order, on a server. 
Each task will take one CPU interval to execute but once a task has finished, 
it has a cooling period during which it can’t be run again. If the cooling period 
for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the 
server needs to finish all tasks.

If at any time the server can’t execute any task then it must stay idle.

Example 1:
Input: [a, a, a, b, c, c], K=2
Output: 7
Explanation: a -> c -> b -> a -> c -> idle -> a

Example 2:
Input: [a, b, a], K=3
Output: 5
Explanation: a -> b -> idle -> idle -> a
"""

from collections import deque
from heapq import heapify, heappop, heappush

def scheduleTasks(tasks, k):
    taskFreq = {}
    for task in tasks:
        taskFreq[task] = taskFreq.get(task, 0) - 1
    maxHeap = [(f, t) for t, f in taskFreq.items()]
    heapify(maxHeap)

    t = 0
    q = deque([]) # [(task, t)]
    while maxHeap or q:
        if maxHeap:
            _, currTask = heappop(maxHeap)
            taskFreq[currTask] += 1
            if taskFreq[currTask] < 0: q.append((currTask, t+1))
        t += 1
        if q and t - q[0][1] >= k:
            prevTask, _ = q.popleft()
            heappush(maxHeap, (taskFreq[prevTask], prevTask))
    return t


if __name__ == "__main__":
    print(scheduleTasks(['a', 'a', 'a', 'b', 'b', 'b'], 2))
    print(scheduleTasks(['a', 'a', 'a', 'b', 'c', 'c'], 2))
    print(scheduleTasks(['a', 'b', 'a'], 3))