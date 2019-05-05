class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l,r = 0,len(nums)-1
        while l<r and nums[l]!=target:
            l+=1
        if l==r and nums[l]!=target:
            return [-1,-1]
        while nums[r]!=target:
            r-=1
        return [l,r]


if __name__ == '__main__':
    y = Solution()
    # h0 = [5,7,7,8,8,10]
    target = 8
    h0 = [5,7,7,8,8,10]
    # target = 6

    print(y.searchRange(h0,target))


