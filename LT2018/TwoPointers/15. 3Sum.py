class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()
        for i in range(len(nums)-1):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            val_i = nums[i]
            while l<r:
                if nums[l] + nums[r] + val_i > 0:
                    r -= 1
                    # continue
                    if nums[l] + nums[r] + val_i == 0:
                        res.append([nums[l], nums[r], val_i])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r -= 1
                if nums[l] + nums[r] + val_i < 0:
                    l += 1

                    # continue
                    print(l, r)
                    if nums[l] + nums[r] + val_i == 0:
                        res.append([nums[l], nums[r], val_i])
                        while l<r and nums[l]==nums[l+1]:
                            l+=1
                        while l<r and nums[r]==nums[r-1]:
                            r -= 1
                l+=1;r-=1
        return res

        # def twoSum(val_nums,val_k):
        #     # if len(val_nums)<=1:
        #     dict_n = {}
        #     for i in range(len(val_nums)):
        #         if val_nums[i] in dict_n:
        #             return [val_k,-val_k - val_nums[i],val_nums[i]]
        #         else:
        #             dict_n[-val_k - val_nums[i]] = i
        #     return []
        # res = []
        # for i in range(len(nums)):
        #     val_sum = nums[i]
        #     val_list = nums[:i]+nums[i+1:]
        #     tmp = twoSum(val_list,val_sum)
        #     if len(tmp)>0:
        #         tmp.sort()
        #         if tmp  not in res:
        #             res.append(tmp)
        # return res


if __name__ == '__main__':
    y = Solution()
    # h0 = [-1, 0, 1, 2, -1, -4]
    # h0= [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
    h0=[3,-2,1,0]
    print(y.threeSum(h0))

    '''
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

    '''


