#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        l,r = 0,len(nums) - 1
        tmpl,tmpr = nums[l],nums[r]
        while l<r:
            if nums[l]!=nums[l-1] and nums[l]<nums[r]:
                res += 1
                # tmpl = nums[l]
                while nums[l]==nums[l+1]:
                    l += 1
            if (r==len(nums)-1 or nums[r]!=nums[r+1])  and nums[l]<nums[r]:
                res += 1
                # tmpr = nums[r]
                while nums[r]==nums[r-1]:
                    r -= 1
            l+=1;r-=1
        if nums[l]==nums[r]:
            res+=1
        return res


if __name__ == '__main__':
    # nums = [1, 1, 2]
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(Solution().removeDuplicates(nums))


    '''
    Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
    '''