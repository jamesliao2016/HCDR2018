#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        aux = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                aux[i][j] = aux[i-1][j]+aux[i][j-1]
        return aux[-1][-1]

if __name__ == '__main__':
    # m = 3; n = 2
    m = 7;
    n = 3
    print(Solution().uniquePaths(m,n))


'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid 
(marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

# 8 apr, 2019
        aux = [[1]*n for _ in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                aux[i][j] = aux[i-1][j] + aux[i][j-1]
        return aux[-1][-1]

# 31 JAN, 2019
        aux = [[1]*n for i in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                aux[i][j] = aux[i-1][j] + aux[i][j-1]
        return aux[-1][-1]
'''