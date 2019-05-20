#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ''
        tmp = zip(*strs)
        for i in tmp:
            if len(set(i))==1:
                res = res + i[0]
            else:
                break
        return res

if __name__ == '__main__':
    ipt = ["flower","flow","flight"]
    print(Solution().longestCommonPrefix(ipt))

    '''
    Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

# 20 MAY, 2019
        tmp = zip(*strs)
        res = ''
        for i in tmp:
            if len(set(i))==1:
                res+=i[0]
            else:
                break
        return res

    '''