#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0,1,2]
        for i in range(2,n+1):
            res.append(res[i-1]+res[i-2])
        return res[-1]

if __name__ == '__main__':
    ipt = 3
    print(Solution().climbStairs(ipt))

'''
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step

# 31 jan, 2019
        res = [0,1,2]
        for i in range(2,n):
            res.append(res[i] + res[i-1])
        return res[-1]

'''