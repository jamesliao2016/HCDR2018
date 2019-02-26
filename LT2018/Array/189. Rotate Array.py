#!/usr/bin/env python2
# coding:utf-8
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if k>len(nums):
            k = k % len(nums)
        for i in range(k):
            nums[0],nums[1:] = nums[-1],nums[:-1]
        return nums

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7]; k = 3
    print(Solution().rotate(nums,k))

    '''
    Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:

Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
Note:

Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
Could you do it in-place with O(1) extra space?

# 20 feb, 2019
        if k>len(nums):
            k = k%len(nums)
        for i in range(k):
            # nums[i],nums[-k+i] = nums[-k+i],nums[i]
            nums[0],nums[1:] = nums[-1],nums[:-1]

    '''