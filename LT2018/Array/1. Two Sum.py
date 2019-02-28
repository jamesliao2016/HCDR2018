class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        tmp = {}
        for i in range(len(nums)):
            if (target - nums[i]) in tmp:
                return [tmp[target - nums[i]],i]
            else:
                tmp[nums[i]] = i


if __name__ == '__main__':
    y = Solution()
    h0 = [2, 7, 11, 15]
    target = 9
    print(y.twoSum(h0,target))

'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

# 27 feb, 2019
        if nums is None:
            return []
        tmp_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in tmp_dict:
                return [i,tmp_dict[target - nums[i]]]
            else:
                tmp_dict[nums[i]] = i

'''
