#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        ll = len(needle)
        for i in range(len(haystack) - ll +1):
            if haystack[i:i+ll] == needle:
                return i
        return -1
if __name__ == '__main__':
    # haystack = "hello"; needle = "ll"
    haystack = "aaaaa"; needle = "bba"
    print(Solution().strStr(haystack,needle))


    '''
    Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
    '''