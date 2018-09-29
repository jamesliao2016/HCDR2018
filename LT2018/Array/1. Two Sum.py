class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if nums is None:
            return []
        tmp_dict = {}
        for i in range(len(nums)):
            if (target - nums[i]) in tmp_dict:
                return [i,tmp_dict[target - nums[i]]]
            else:
                tmp_dict[nums[i]] = i


if __name__ == '__main__':
    y = Solution()
    h0 = [2, 7, 11, 15]
    target = 9
    print(y.twoSum(h0,target))


