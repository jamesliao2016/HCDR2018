#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m,n = len(matrix), len(matrix[0])
        def dfs(i,j):
            if res[i][j] == 0:
                val = matrix[i][j]
                res[i][j] = 1 + \
                    max(dfs(i+1,j) if i+1 < m and val > matrix[i+1][j] else 0, \
                        dfs(i - 1, j) if i - 1 >=0 and val > matrix[i - 1][j] else 0, \
                        dfs(i, j+1) if j + 1 < n and val > matrix[i][j+1] else 0, \
                        dfs(i, j-1) if j-1 >=0 and val > matrix[i][j-1] else 0)
            return res[i][j]
        res = [[0]*len(matrix[0]) for i in range(len(matrix))]
        return max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))

if __name__ == '__main__':
    ipt = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
    print(Solution().longestIncreasingPath(ipt))


    '''
    Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

    '''