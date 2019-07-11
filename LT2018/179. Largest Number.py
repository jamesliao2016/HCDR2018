class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(x) for x in nums]
        tmp = [len(x) for x in nums]
        longest = max(tmp)
        nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
        if nums and nums[0] == '0':
            return '0'
        return ''.join(nums)

if __name__ == '__main__':
    inputx = [3,30,34,5,9]
    print(Solution().largestNumber(inputx))
    '''
    Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"
Example 2:

Input: [3,30,34,5,9]
Output: "9534330"
Note: The result may be very large, so you need to return a string instead of an integer.

Accepted
133,606
Submissions
513,104

# 11 july, 2019

        nums = [str(x) for x in nums]
        longest = max([len(x) for x in nums], default=0)
        nums.sort(key=lambda x: x*(longest//len(x)+1), reverse=True)
        if nums and nums[0] == '0':
            return '0'
        return ''.join(nums)

    '''