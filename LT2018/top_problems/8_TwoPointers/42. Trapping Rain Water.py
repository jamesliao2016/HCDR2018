#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        l,r = 0,len(height)-1
        minval = 0
        while l<r:
            while l<r and minval>=height[l]:
                res += (minval - height[l])
                l += 1
            while l<r and minval>=height[r]:
                res += (minval - height[r])
                r -= 1
            minval = min(height[l],height[r])
        return res


if __name__ == '__main__':
    ipt = [0,1,0,2,1,0,1,3,2,1,2,1]
    print(Solution().trap(ipt))

'''

# 14 may, 2019
        l,r = 0,len(height)-1
        min_h = 0
        res = 0
        while l<r:
            while l<r and height[r]<=min_h:
                res += min_h - height[r]
                r-=1
            while l<r and height[l]<=min_h:
                res += min_h - height[l]
                l+=1
            min_h = min(height[l],height[r])
        return res

'''