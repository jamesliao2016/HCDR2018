#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0,0
        for i in nums:
            l,r = r,max(r,l+i)
        return r

if __name__ == '__main__':
    # ipt = [1,2,3,1]
    ipt = [2,7,9,3,1]
    print(Solution().rob(ipt))