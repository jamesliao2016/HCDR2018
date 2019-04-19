#!/usr/bin/env python2
# coding:utf-8

'''
Given two strings s and t , write a function to determine if t is an anagram of s.
'''

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s) == sorted(t)


if __name__ == '__main__':
    # s = "anagram"; t = "nagaram"
    s = "rat"; t = "car"

    print(Solution().isAnagram(s,t))

'''
# 16 apr, 2019
        return sorted(s)==sorted(t)

'''