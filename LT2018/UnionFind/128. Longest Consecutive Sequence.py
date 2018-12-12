#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        res = 1
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    tmp += 1
                else:
                    res = max(res,tmp)
                    tmp = 1
        return max(res,tmp)

if __name__ == '__main__':
    ipt = [100, 4, 200, 1, 3, 2]
    print(Solution().longestConsecutive(ipt))


    '''
    Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

12 dec

        if len(nums)==0:
            return 0
        nums.sort()
        res = 1
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i-1]:
                if nums[i] == nums[i-1]+1:
                    tmp += 1
                else:
                    res = max(res,tmp)
                    tmp = 1
        return max(res,tmp)

    '''