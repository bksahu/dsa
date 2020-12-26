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

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')


def find_employee_free_time(schedules):
    # Time Complexity: O(nlogn) where n is
    # no. of employee timings
    result, merged = [], []
    schedule = []
    for employee in schedules:
        for time in employee:
            schedule.append(time)
    schedule.sort(key=lambda x: x.start)
    start = schedule[0].start
    end = schedule[0].end

    for i in range(1, len(schedule)):
        if schedule[i].start <= end:
            end = max(end, schedule[i].end)
        else:
            merged.append(Interval(start, end))
            start = schedule[i].start
            end = schedule[i].end
    merged.append(Interval(start, end))

    for i in range(1, len(merged)):
        result.append(Interval(merged[i-1].end, merged[i].start))

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
