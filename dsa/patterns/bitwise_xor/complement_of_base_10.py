"""
Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” 
in binary and 7 as “0111” in binary.

The complement of a binary representation is the number in binary that we get when we change every 1 
to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

For a given positive number N in base-10, return the complement of its binary representation as a base-10 
integer.

Example 1:
Input: 8
Output: 7
Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.

Example 2:
Input: 10
Output: 5
Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.
"""


# intuition: add the compliments to get 2**n - 1 where n is no. of bits
# example: 1000 (8) + 0001 (7) = 1111 (15)
def calculate_bitwise_complement(N):
    if N == 0:
        return 1
    bits = 0
    n = N
    while n:
        bits += 1
        n = n >> 1

    bound = pow(2, bits) - 1
    return bound ^ N # bound - N



if __name__ == "__main__":
    print(calculate_bitwise_complement(8))
    print(calculate_bitwise_complement(10))
