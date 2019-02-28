#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)<=1:
            return 0
        l,r = 0,len(nums)-1
        while l<=r:
            mid = int((l+r)/2)
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            else:
                if nums[mid]<nums[mid+1]:
                    l = mid+1
                else:
                    r = mid - 1
        return l if nums[l]>nums[r] else r

if __name__ == '__main__':
    # ipt = [1,2,1,3,5,6,4]
    ipt = [1]
    print(Solution().findPeakElement(ipt))

'''
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5 
Explanation: Your function can return either index number 1 where the peak element is 2, 
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

# 18 feb, 2019
        l,r = 0,len(nums)-1
        while l<r:
            mid = int((l+r)/2)
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            else:
                if nums[mid] <= nums[mid-1]:
                    r = mid
                if nums[mid] <= nums[mid+1]:
                    l = mid
        return l


15 feb, 2019
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

'''