#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m,n=0,len(matrix[0])-1
        while m<len(matrix) and n>=0:
            if matrix[m][n] == target:
                return True
            if matrix[m][n] > target:
                n-=1
            else:
                m+=1
        return False
if __name__ == '__main__':
    ipt = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    # nn=20
    nn=5
    print(Solution().searchMatrix(ipt,nn))

    '''
    Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


    '''