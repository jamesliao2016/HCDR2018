#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not max(matrix):
            return False
        l, r = 0, len(matrix[0]) - 1
        while l>=0 and l<len(matrix) and r>=0 and r<len(matrix[0]):
            if matrix[l][r] == target:
                return True
            elif matrix[l][r] > target:
                r -= 1
            else:
                l+=1
        return False

if __name__ == '__main__':
    ipt = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
    nn=20
    # nn=5
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

# 4 jan, 2019
        if len(matrix)==0:
            return False
        if len(matrix)==1:
            return target in matrix[0]
        l,r = 0,len(matrix[0])-1
        while l>=0 and l<len(matrix) and r>=0 and r<len(matrix[0]):
            if matrix[l][r]==target:
                return True
            if matrix[l][r] > target:
                r -= 1
            else:
                l += 1
        return False

# 12 dec

        m,n=0,len(matrix[0])-1
        while m<len(matrix) and n>=0:
            if matrix[m][n] == target:
                return True
            if matrix[m][n] > target:
                n-=1
            else:
                m+=1
        return False
        
    '''