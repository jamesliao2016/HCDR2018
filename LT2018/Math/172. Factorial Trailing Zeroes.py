#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<5:
            return 0
        return int(n/5) + self.trailingZeroes(int(n/5))

if __name__ == '__main__':
    n = 5
    print(Solution().trailingZeroes(n))
'''
Given an integer n, return the number of trailing zeroes in n!.

Example 1:

Input: 3
Output: 0
Explanation: 3! = 6, no trailing zero.
Example 2:

Input: 5
Output: 1
Explanation: 5! = 120, one trailing zero.
Note: Your solution should be in logarithmic time complexity.

#jan 1 2019
        if n < 5:
            return 0
        return int(n / 5) + self.trailingZeroes(int(n / 5))

'''