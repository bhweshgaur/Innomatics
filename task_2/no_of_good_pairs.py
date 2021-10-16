# Number of Good Pairs
'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
 

Constraints:

1 <= nums.length <= 100
1 <= nums[i] <= 100
'''

# Code

def numIdenticalPairs(nums: List[int]) -> int:
        temp_dict = {}
        for n in set(nums):
            temp_dict[n] = nums.count(n)
            
        for key, value in temp_dict.items():
            temp_dict[key] = value*(value - 1)//2
            
        return sum(temp_dict.values())