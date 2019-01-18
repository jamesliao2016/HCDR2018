#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(1,len(nums)):
            nums[i] += max(nums[i-1],0)
        return max(nums)

if __name__ == '__main__':
    da_ipt = [-2,1,-3,4,-1,2,1,-5,4]
    # da_ipt = [-2,1]
    # da_ipt = [-2]
    da_opt = Solution()
    print(da_opt.maxSubArray(da_ipt))

'''
Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the 
divide and conquer approach, which is more subtle.

# 18 JAN, 2019
        for i in range(1,len(nums)):
            nums[i] = max(nums[i],(nums[i] + nums[i-1]))
        return max(nums)


# 17 jan, 2019
        l,r = 0,0
        res = sum(nums[l:r+1])
        val_del = 0
        while l<r:
            tmp_sum = sum(nums[l:r+1])
            if val_del >= 0 and r<len(nums):
                r += 1
            else:
                l += 1
            tmp_sum_up = sum(nums[l:r+1])
            val_del = tmp_sum_up - tmp_sum
            res = max(res, max(tmp_sum_up,tmp_sum))
        return res

'''