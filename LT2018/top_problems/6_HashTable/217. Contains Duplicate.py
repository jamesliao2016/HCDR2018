#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """


if __name__ == '__main__':
    ipt = [1,1,1,3,3,4,3,2,4,2]
    print(Solution().containsDuplicate(ipt))


'''
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array, 
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true

# 27 feb, 2019
return not len(nums) == len(set(nums))
'''