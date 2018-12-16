#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r=0,len(nums)-1
        while l<r-1:
            mid = int((l+r)/2)
            if nums[mid]>=nums[mid-1] and nums[mid]>=nums[mid+1]:
                return mid
            if nums[mid]<nums[mid+1]:
                l=mid
            if nums[mid]<nums[mid-1]:
                r=mid
        return l if nums[l]>nums[r] else r

if __name__ == '__main__':
    # ipt = [1,2,1,3,5,6,4]
    ipt = [1]
    print(Solution().findPeakElement(ipt))