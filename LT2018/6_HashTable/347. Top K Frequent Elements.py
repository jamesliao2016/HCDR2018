#!/usr/bin/env python2
# coding:utf-8
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import Counter
        return [i for i,j in Counter().most_common(nums,k)]

if __name__ == '__main__':

    '''
    Given a non-empty array of integers, return the k most frequent elements.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
Note:

You may assume k is always valid, 1 ≤ k ≤ number of unique elements.
Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

# 27 mar, 2019
        from collections import Counter
        return [i for i,j in Counter(nums).most_common(k)]

    '''