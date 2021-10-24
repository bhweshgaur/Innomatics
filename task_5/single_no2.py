# Single Number II

'''
You must implement a solution with a linear runtime complexity and use only constant extra space.

 

Example 1:

Input: nums = [2,2,3,2]
Output: 3
Example 2:

Input: nums = [0,1,0,1,0,1,99]
Output: 99
 

Constraints:

1 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each element in nums appears exactly three times except for one element which appears once.
'''


def singleNumber(nums: List[int]) -> int:
    num_count_dict = {}
    
    for i in nums:
        if i in num_count_dict.keys():
            num_count_dict[i] += 1
        else:
            num_count_dict[i] = 1
            
    keys, values = list(num_count_dict.keys()), list(num_count_dict.values())
    
    for index in range(len(values)):
        if values[index] == 1:
            return keys[index]