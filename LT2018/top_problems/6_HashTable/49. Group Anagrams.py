#!/usr/bin/env python2
# coding:utf-8

class Solution(object):
    def __init__(self,x):
        self.x = x
    def groupAnagrams(self,strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        tmp_dict = {}
        res = []
        for i in strs:
            tmp_i = ''.join(sorted(i))
            if tmp_i not in tmp_dict:
                tmp_dict[tmp_i] = [i]
            else:
                tmp_dict[tmp_i].append(i)
        for j in tmp_dict:
            res.append(tmp_dict[j])
        return res

if __name__ == '__main__':
    input_x = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print(Solution(input_x).groupAnagrams())

    '''
    Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.

# 29 mar, 2019
        res = []
        tmp_dict = {}
        for i in strs:
            tmp = ''.join(sorted(i))
            if tmp not in tmp_dict:
                tmp_dict[tmp] = [i]
            else:
                tmp_dict[tmp].append(i)
        for j in tmp_dict:
            res.append(tmp_dict[j])
        return res

    '''