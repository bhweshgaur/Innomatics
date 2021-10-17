# Counting Bits
'''
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101
 

Constraints:

0 <= n <= 105

'''

# Code
def countBits(n: int) -> List[int]:
    output = []
    for i in range(n+1):
        n_bin = list(bin(i).replace('0b',''))
        n_bin = [int(k) for k in n_bin]
        output.append(sum(n_bin))
    return output