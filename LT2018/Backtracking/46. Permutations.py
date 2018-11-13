#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = [[]]
        for i in nums:
            tmp_res = []
            for j in res:
                for k in range(len(j)+1):
                    tmp_res.append(j[k:]+[i]+j[:k])
            res = tmp_res
        return res

if __name__ == '__main__':
    data_input = [1,2,3]
    data_output = Solution()
    print(data_output.permute(data_input))