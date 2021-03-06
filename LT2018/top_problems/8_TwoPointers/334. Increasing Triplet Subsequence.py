#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l,r = float('inf'),float('inf')
        for i in nums:
            if i<l:
                l = i
            if i<r and i>l:
                r = i
            if i>r:
                return True
        return False

if __name__ == '__main__':
    # ipt = [1,2,3,4,5]
    # ipt = [5,4,3,2,1]
    # ipt = [1,2,-1,5,7]
    ipt = [1,2,-1,-5,-3,-2]
    print(Solution().increasingTriplet(ipt))

    '''
    Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:

Return true if there exists i, j, k 
such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:

Input: [1,2,3,4,5]
Output: true
Example 2:

Input: [5,4,3,2,1]
Output: false

# 17 APR, 2019
        l,r = float('inf'),float('inf')
        for i in nums:
            if i<l:
                l = i
            if i<r and i>l:
                r = i
            if i>r:
                return True
        return False

# 16 apr, 2019
        l,r = float('inf'),float('inf')
        for i in nums:
            if i<l:
                l = i
            if i>l and i<r:
                r = i
            if i > r:
                return True
        return False

# 27 MAR, 2019
        l,r = float('inf'),float('inf')
        for i in nums:
            if i<l:
                l = i
            if i>l and i<r:
                r = i
            if i>r:
                return True
        return False


# 26 mar, 2019
        l,r = float('inf'),float('inf')
        for i in nums:
            if l>=i:
                l=i
            else:
                if r>=i:
                    r=i
                else:
                    return True
        return False

# 8 jan, 2019
        l = r = float('inf')
        for i in nums:
            if i<=l:
                l = i
                continue
            if i<=r:
                r = i
            if i>r:
                return True
        return False


# 7 jan, 2019

        l = r = float('inf')
        for i in nums:
            if l>=i:
                l = i
            if r>=i:
                r = i
            else:
                return True
        return False

    '''