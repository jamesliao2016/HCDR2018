#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            tmp = ord(s[i]) - ord('A') + 1
            tmp = tmp * pow(26,(len(s) - i - 1))
            res += tmp
        return res
if __name__ == '__main__':

'''
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''