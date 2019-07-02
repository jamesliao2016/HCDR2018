#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        nums.sort()
        res = 0
        tmp_res = 1
        for i in range(1,len(nums)):
            if nums[i-1] != nums[i]:
                if nums[i] == nums[i-1]+1:
                    tmp_res += 1
                else:
                    res = max(res,tmp_res)
                    tmp_res = 1
        return max(res,tmp_res)

if __name__ == '__main__':
    # ipt = [100, 4, 200, 1, 3, 2]
    ipt = [1,2,0,1]
    print(Solution().longestConsecutive(ipt))


    '''
    Given an unsorted array of integers, find the length of the longest 
    consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.







# 2 july, 2019
        if not nums:
            return 0
        nums.sort()
        res = 1
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i]==nums[i-1]+1:
                    tmp +=1
                else:
                    tmp = 1
                res = max(res,tmp)
        return res

13 feb, 2019
        res = 0
        nums.sort()
        res_tmp = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                res_tmp =1
            else:
                res_tmp+=1
            res = max(res,res_tmp)
        return res

12 feb, 2019

        nums.sort()
        res = 1
        tmp = 1
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]:
                if nums[i] == nums[i - 1]+1:
                    tmp += 1
                else:
                    res = max(res,tmp)
                    tmp = 1
        return max(res,tmp)

14 dec

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