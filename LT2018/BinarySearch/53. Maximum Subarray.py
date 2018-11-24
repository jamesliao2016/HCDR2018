#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

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

if __name__ == '__main__':
    # da_ipt = [-2,1,-3,4,-1,2,1,-5,4]
    # da_ipt = [-2,1]
    da_ipt = [-2]
    da_opt = Solution()
    print(da_opt.maxSubArray(da_ipt))