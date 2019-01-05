#!/usr/bin/env python2
# coding:utf-8


class Solution:
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = [1]*len(nums)
        p = nums[0]
        for i in range(1,len(nums)):
            res[i] = res[i]*p
            p=p*nums[i]
        p = nums[-1]
        for i in range(len(nums)-2,-1,-1):
            res[i] = res[i]*p
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

# 5 Jan, 2019
        res = [1]*len(nums)
        p = 1
        for i in range(1,len(nums)):
            p = p * nums[i-1]
            res[i] = res[i] * p
        p = 1
        for j in range(len(nums)-2,-1,-1):
            p = p * nums[j+1]
            res[j] = res[j] * p
        return res

# 4 Jan, 2019
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

    '''
