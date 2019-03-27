#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        stack = []
        for i in matrix:
            stack = stack + i
        stack.sort()
        return stack[k-1]


if __name__ == '__main__':
#     ipt = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ]
#     k = 8
#     ipt = [[1,2],[1,3]];k=1
    ipt =[[1,3,5],[6,7,12],[11,14,14]];k=3
    print(Solution().kthSmallest(ipt,k))

'''
Given a n x n matrix where each of the rows and columns are sorted in ascending order, 
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note: 
You may assume k is always valid, 1 ≤ k ≤ n2.

# 27 mar, 2019
        res = []
        for i in matrix:
            res +=i
        return sorted(res)[k-1]


# 9 jan, 2019
        l=[]
        for i in matrix:
            l+=i
            if len(l)>k:
                break
        return sorted(l)[k-1]

        if not matrix or not matrix[0]:
            return 0
        def dfs(i,j,st,res=[]):

            if (st <= (i+1)*(i+1) or st <= (j+1)*(j+1)) and (st > i*i and st > j*j):
                if tmplist[i][j]==0:
                    res.append(matrix[i][j])
                    tmplist[i][j]=1
            if i+1<len(matrix):
                dfs(i+1,j,st,res)
            if st>0 and j-1<len(matrix[0]):
                dfs(i,j+1,st,res)

        res = []
        lenmt = len(matrix)
        tmplist = [[0] *lenmt for i in range(lenmt)]
        dfs(0,0,k,res)
        l=0
        for i in range(len(matrix)):
            if i*i<k and (i+1)*(i+1)>=k:
                l=i
        tmp = l*l
        tmp1 = [0]*tmp
        # res = list(set(res))
        res.sort()
        res = tmp1+res
        return res[k-1]
        # return res
'''