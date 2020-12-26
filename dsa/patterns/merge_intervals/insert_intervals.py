"""
Given a list of non-overlapping intervals sorted by their start time, 
insert a given interval at the correct position and merge all necessary 
intervals to produce a list that has only mutually exclusive intervals.

Example 1:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,6]
Output: [[1,3], [4,7], [8,12]]
Explanation: After insertion, since [4,6] overlaps with [5,7], we merged them into one [4,7].

Example 2:
Input: Intervals=[[1,3], [5,7], [8,12]], New Interval=[4,10]
Output: [[1,3], [4,12]]
Explanation: After insertion, since [4,10] overlaps with [5,7] & [8,12], we merged them into [4,12].

Example 3:
Input: Intervals=[[2,3],[5,7]], New Interval=[1,4]
Output: [[1,4], [5,7]]
Explanation: After insertion, since [1,4] overlaps with [2,3], we merged them into one [1,4].
"""

# def insert(intervals, new_interval):
#     merged = []

#     for i, interval in enumerate(intervals):
#         if new_interval[0] < interval[0]:
#             intervals.insert(i, new_interval)   
#             break
#     if i == len(intervals)-1:
#         intervals.append(new_interval)
    
#     start = intervals[0][0]
#     end = intervals[0][1]

#     for i in range(1, len(intervals)):
#         interval_start = intervals[i][0]
#         interval_end = intervals[i][1]
#         if interval_start <= end:
#             end = max(interval_end, end)
#         else:
#             merged.append([start, end])
#             start = interval_start
#             end = interval_end
#     merged.append([start, end])
#     return merged

def insert(intervals, new_interval):
    merged = []
    i, start, end = 0, 0, 1
    while i < len(intervals) and new_interval[start] > intervals[i][end]:
        merged.append(intervals[i])
        i += 1

    while i < len(intervals) and intervals[i][start] <= new_interval[end] :
        new_interval[start] = min(intervals[i][start], new_interval[start])
        new_interval[end] = max(intervals[i][end], new_interval[end])
        i += 1
    merged.append(new_interval)

    while i < len(intervals):
        merged.append(intervals[i])
        i += 1

    return merged

if __name__ == "__main__":
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 6])))
    print("Intervals after inserting the new interval: " + str(insert([[1, 3], [5, 7], [8, 12]], [4, 10])))
    print("Intervals after inserting the new interval: " + str(insert([[2, 3], [5, 7]], [1, 4])))

