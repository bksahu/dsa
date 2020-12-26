"""
For ‘K’ employees, we are given a list of intervals representing the working hours 
of each employee. Our goal is to find out if there is a free interval that is common 
to all employees. You can assume that each list of employee working hours is sorted on 
the start time.

Example 1:
Input: Employee Working Hours=[[[1,3], [5,6]], [[2,3], [6,8]]]
Output: [3,5]
Explanation: Both the employess are free between [3,5].

Example 2:
Input: Employee Working Hours=[[[1,3], [9,12]], [[2,4]], [[6,8]]]
Output: [4,6], [8,9]
Explanation: All employess are free between [4,6] and [8,9].

Example 3:
Input: Employee Working Hours=[[[1,3]], [[2,4]], [[3,5], [7,9]]]
Output: [5,7]
Explanation: All employess are free between [5,7].
"""

from heapq import *

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


class EmployeeInterval:
    def __init__(self, interval, employeeIndex, intervalIndex):
        self.interval = interval
        self.employeeIndex = employeeIndex
        self.intervalIndex = intervalIndex

    def __lt__(self, other):
        return self.interval.start < other.interval.start


def find_employee_free_time(schedule):
    # Time Complexity: O(nlogk) where n is
    # no. of employee timings and k in the 
    # no. of employees. Note: k <= n
    result = []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))
    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        # if previousInterval is not overlapping with the next interval, insert a free interval
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            previousInterval = queueTop.interval
        else:  # overlapping intervals, update the previousInterval if needed
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))

    return result



if __name__ == "__main__":
    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()
