#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i-1,-1):
                if nums[j]>nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)


if __name__ == '__main__':
    ipt = [10,9,2,5,3,7,101,18]
    print(Solution().lengthOfLIS(ipt))

    '''
    Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4 
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?
    '''
