#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        res = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(i+1,len(nums)):
                if nums[i]<nums[j]:
                    res[i] = max(res[i],res[j]+1)
        return max(res)

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

# 7 jan, 2019
        if not nums:
            return 0
        res = [1]*len(nums)
        # for i in range(len(nums)):
        for j in range(len(nums)-1,-1,-1):
            tmp0 = nums[j+1:]
            tmp1 = res[j+1:]
            for k in range(j+1,len(nums)):
                if nums[j]<nums[k]:
                    res[j] = max(res[j],(res[k]+1))
        return max(res)
        # return res


# 6 jan, 2019
        dp = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i-1,-1):
                if nums[i]<nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)


# 12 dec

        dp = [1]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            for j in range(len(nums)-1,i-1,-1):
                if nums[j]>nums[i]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)

    '''
