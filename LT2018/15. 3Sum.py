class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = []
        # nums.sort()
        # for i in range(len(nums) - 2):
        #     if nums[i] == nums[i-1]:
        #         continue
        #     tmp0 = nums[i]
        #     for j in range(i+1,len(nums) - 1):
        #         tmp1 = nums[j]
        #         for k in range(j+1,len(nums)):
        #             tmp2 = nums[k]
        #             if tmp0 + tmp1 + tmp2 == 0:
        #                 res.append([tmp0,tmp1,tmp2])
        # return res

        res = []

        nums.sort()
        for i in range(len(nums)-1):
            if i >0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums) -1
            while l<r:
                tmp = nums[i] + nums[l] + nums[r]
                if tmp > 0:
                    r -= 1
                    continue
                if tmp < 0:
                    l += 1
                    continue
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l<r and nums[l] == nums[l+1]:
                        l +=1
                    while l<r and nums[r] == nums[r-1]:
                        r -= 1
                l += 1; r-=1
        return res


if __name__ == '__main__':
    y = Solution()
    h0 = [-1, 0, 1, 2, -1, -4]
    print(y.threeSum(h0))


