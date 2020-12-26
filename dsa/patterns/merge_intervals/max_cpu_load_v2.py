'''
We are given a list of Jobs. Each job has a Start time, an End time, and a CPU load when 
it is running. Our goal is to find the maximum CPU load at any time if all the jobs are 
running on the same machine.

Example 1:
Jobs: [[1,4,3], [2,5,4], [7,9,6]]
Output: 7
Explanation: Since [1,4,3] and [2,5,4] overlap, their maximum CPU load (3+4=7) will be when both the 
jobs are running at the same time i.e., during the time interval (2,4).

Example 2:
Jobs: [[6,7,10], [2,4,11], [8,12,15]]
Output: 15
Explanation: None of the jobs overlap, therefore we will take the maximum load of any job which is 15.

Example 3:
Jobs: [[1,4,2], [2,4,1], [3,6,5]]
Output: 8
Explanation: Maximum CPU load will be 8 as all jobs overlap during the time interval [3,4]. 
'''


def find_max_cpu_load(starts, ends, loads):
    starts.sort()
    ends.sort()
    max_load = loads[0]
    i, j = 1, 0
    res = 0

    while i < len(starts) and j < len(ends):
        if starts[i] <= ends[j]:
            max_load += loads[i]
            i += 1
        else:
            max_load -= loads[j]
            j += 1

        res = max(res, max_load)


    return res


if __name__ == "__main__":
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([1,2,7], [4,5,9], [3,4,6])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([6,2,8], [7,4,12], [10,11,15])))
    print("Maximum CPU load at any time: " + str(find_max_cpu_load([1,2,3], [4,4,6], [2,1,5])))

