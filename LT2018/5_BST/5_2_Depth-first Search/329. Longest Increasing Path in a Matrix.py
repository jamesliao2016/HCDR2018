#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0
        res = [[1]*len(matrix[0]) for i in range(len(matrix))]

        def dfs(i,j):
            if res[i][j]==1:
                tmp = matrix[i][j]
                res[i][j]+= max(dfs(i+1,j) if i+1<len(matrix) and matrix[i+1][j]>tmp else 0,\
                                dfs(i-1,j) if i-1>=0 and matrix[i-1][j]>tmp else 0,\
                                dfs(i,j+1) if j+1<len(matrix[0]) and matrix[i][j+1]>tmp else 0,\
                                dfs(i,j-1) if j-1>=0 and matrix[i][j-1]>tmp else 0)
            return res[i][j]
        return max([dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0]))])

if __name__ == '__main__':
    ipt = [
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
    # ipt = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]
    print(Solution().longestIncreasingPath(ipt))


    '''
    Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down. 
You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

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

# 26 MAR, 2019
        if not matrix or not matrix[0]:
            return 0
        # res = [[1]*len(matrix[0])]*len(matrix)
        res = [[1]*len(matrix[0]) for i in range(len(matrix))]
        def dfs(i,j):
            if res[i][j] == 1:
                tmp = matrix[i][j]
                res[i][j] += max(dfs(i+1,j) if i+1 < len(matrix) and matrix[i+1][j]>tmp else 0,
                                 dfs(i-1,j) if i-1 >= 0 and matrix[i-1][j] > tmp else 0,
                                 dfs(i,j+1) if j+1 < len(matrix[0]) and matrix[i][j+1]>tmp else 0,
                dfs(i,j-1) if j-1 >= 0 and matrix[i][j-1] > tmp else 0)
            return res[i][j]
        return max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))

# 22 mar, 2019
        if not matrix or not matrix[0]:
            return 0
        res = [[1]*len(matrix[0]) for i in range(len(matrix))]

        def dfs(i,j):
            tmp = matrix[i][j]
            if res[i][j]==1:
                res[i][j] += max(dfs(i+1,j) if i+1<len(matrix) and matrix[i+1][j]>tmp else 0, \
                                 dfs(i - 1, j) if i - 1 >=0 and matrix[i - 1][j] > tmp else 0, \
                                 dfs(i, j+1) if j + 1 < len(matrix[0]) and matrix[i][j+1] > tmp else 0, \
                                 dfs(i, j-1) if j - 1 >= 0 and matrix[i][j-1] > tmp else 0)
            return res[i][j]
        return max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))


# 8 jan, 2019
        if not matrix or not matrix[0]:
            return 0
        def dfs(i,j):
            if res[i][j]==0:
                tmp = [dfs(i+1,j) if i+1<len(matrix) and matrix[i+1][j]>matrix[i][j] else 0, \
                       dfs(i - 1, j) if i - 1 >=0 and matrix[i - 1][j] > matrix[i][j] else 0, \
                       dfs(i, j+1) if j + 1 < len(matrix[0]) and matrix[i][j+1] > matrix[i][j] else 0, \
                       dfs(i, j-1) if j - 1 >=0 and matrix[i][j-1] > matrix[i][j] else 0]
                res[i][j] =res[i][j]+max(tmp)+1
            return res[i][j]
        res = [[0]*len(matrix[0]) for i in range(len(matrix))]
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[0])):
        #         dfs(i,j)
        return max(dfs(i,j) for i in range(len(matrix)) for j in range(len(matrix[0])))

# 7 jan, 2019
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

    '''