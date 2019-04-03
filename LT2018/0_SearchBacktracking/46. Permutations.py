#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            tmp = []
            for j in res:
                for k in range(len(j)+1):
                    tmp.append(j[k:]+[i]+j[:k])
            res = tmp
        return res

if __name__ == '__main__':
    data_input = [1,2,3]
    data_output = Solution()
    print(data_output.permute(data_input))

    '''
    Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

# 3 apr, 2019
        res = [[]]
        for i in nums:
            tmp = []
            for j in res:
                for k in range(len(j)+1):
                    tmp.append(j[k:-1]+[i]+j[:k])
            res = tmp
        return res

# 2 apr,2019
        res = [[]]
        for i in nums:
            tmp = []
            for j in res:

                for k in range(len(j)+1):
                    tmp.append(j[k:]+[i]+j[:k])
            res = tmp
        return res


    5 dec
            res = [[]]
        for i in nums:
            tmp_res = []
            for j in res:
                for k in range(len(j)+1):
                    tmp_res.append(j[k:]+[i]+j[:k])
            res = tmp_res
        return res

    '''