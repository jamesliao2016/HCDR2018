#!/usr/bin/env python2
# coding:utf-8


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        p = 1
        for i in nums:
            res.append(p)
            p = p*i
        p = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i] * p
            p = p * nums[i]
        return res


if __name__ == '__main__':
    ipt = [1,2,3,4]
    print(Solution().productExceptSelf(ipt))

    '''
    Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:

    Input:  [1,2,3,4]
    Output: [24,12,8,6]
    Note: Please solve it without division and in O(n).


    '''
