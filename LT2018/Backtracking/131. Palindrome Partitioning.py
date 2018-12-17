#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:i+1] ] + rest\
                 for i in range(len(s))\
                 if s[:i+1] == s[i::-1] \
                for rest in self.partition(s[i+1:])] or [[]]

if __name__ == '__main__':
    ipt ="aab"
    print(Solution().partition(ipt))

    '''
    Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

# dec 17
        res = [[s[:i]] + rest \
               for i in range(1,len(s)+1)  if s[:i]==s[i-1::-1]\
               for rest in self.partition(s[i:])]
        return res or [[]]

    '''