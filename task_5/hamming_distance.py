# Hamming Distance
'''
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.

Given two integers x and y, return the Hamming distance between them.

 

Example 1:

Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
Example 2:

Input: x = 3, y = 1
Output: 1
 

Constraints:

0 <= x, y <= 231 - 1
'''



def hammingDistance(x: int, y: int) -> int:
    def getBinary(n):
        b = ''
        while n > 0:
            d = n%2
            b = str(d)+b
            n = n//2
        return b

    b_x = getBinary(x)
    b_y = getBinary(y)
    
    count = 0
    if b_x == b_y:
        return count
    else:
        if len(b_x)>len(b_y):
            b_y = '0'*(len(b_x)-len(b_y)) + b_y
        else:
            b_x = '0'*(len(b_y) - len(b_x)) + b_x
            
            
    for i, j in zip(b_x, b_y):
        if i != j:
            count+=1
            
    return count