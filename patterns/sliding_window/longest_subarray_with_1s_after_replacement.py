"""
Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, 
find the length of the longest contiguous subarray having all 1s.

Example 1:
Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
Output: 6
Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.

Example 2:
Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
Output: 9
Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.
"""

def solution(a, k):
    win_start, max_len = 0, 0
    no_of_zeros = 0

    for win_end in range(len(a)):
        # import ipdb; ipdb.set_trace()
        if a[win_end] == 0:
            no_of_zeros += 1
        
        # Using if intead of while loop because the max size will not DECREASE
        # anymore but will INCREASE or be SAME because we are increamenting 
        # win_star everytime until no_of_zeros > k. For example, 
        # a = [1,1,1,0,0,0,0,0...], k=2 the window size is always going to be 5. 
        # Another example a = [1,1,1,0,0,0......,1,1,1,1] is going to be 5 
        # untill win_end meets the first of the last 1s then max_len is 
        # suddenly going to change to 6
        if no_of_zeros > k: 
            left_num = a[win_start]
            if left_num == 0:
                no_of_zeros -= 1
            win_start += 1

        max_len = max(max_len, win_end - win_start + 1)
    return max_len


if __name__ == "__main__":
    print(solution([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2))
    print(solution([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3))
