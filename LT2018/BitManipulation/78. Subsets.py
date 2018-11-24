#!/usr/bin/env python2
# coding:utf-8

'''
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.
'''

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(1 << len(nums)):
            tmp = []
            for j in range(len(nums)):
                # print(1<<j&i)
                # print(i&1 << j)
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
                    print(i,j)
            # print(tmp)
            # print(i)
            # print(j)
            res.append(tmp)
            # print(res)
        return res


if __name__ == '__main__':
    nums = [1, 2, 3]
    print(Solution().subsets(nums))