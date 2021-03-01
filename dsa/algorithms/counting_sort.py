"""
Counting Sort

* Works when we have limited set of numbers in the array.
* Stable
* Time: O(n + k)
* Space: O(n + k)
where n is size of array and k is the number of unique numbers in it

Algorithm: [1, 0, 3, 1, 3, 1]
1. Build frequency array where ith index has number of elements type i
[1, 3, 0, 2]

2. Find prefix sum
[1, 4, 4, 6]

3. Shift it to right by 1
[0, 1, 4, 4]
This array means that:
-> There are 0 elements before num = 0
-> There are 1 elements before num = 1
-> There are 4 elements before num = 2
-> There are 4 elements before num = 3

4. Iterate through the origin array and add the nums
to it's right index using the previous array we build.
Everytime you add a number to output array, add +1 to
prefix array, since that position is filled we start from
next position when we again encounter that same number
"""

def countingSort(nums):
    rangeOfNums = max(nums) - min(nums) + 1
    prefix = [0]*(rangeOfNums + 1)

    for num in nums:
        prefix[num+1] += 1
    
    for i in range(1, len(prefix)):
        prefix[i] += prefix[i-1]

    ret = [0]*len(nums)
    for num in nums:
        ret[prefix[num]] = num
        prefix[num] += 1

    return ret


if __name__ == "__main__":
    print(countingSort([1, 0, 3, 1, 3, 1]))