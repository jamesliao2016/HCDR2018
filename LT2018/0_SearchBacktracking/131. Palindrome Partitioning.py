#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        return [[s[:idx+1]] + tmp\
                for idx in range(len(s))\
                if s[:idx+1] == s[:idx+1][::-1]\
                for tmp in self.partition(s[idx+1:])] or [[]]

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






# 9 apr, 2019
        return [[s[:idx+1]] + tmp \
                for idx in range(len(s)) \
                if s[:idx+1]==s[:idx+1][::-1] \
                for tmp in self.partition(s[idx+1:]) \
                ] or [[]]

# 13 feb, 2019
        return [[s[:idx+1]] + rest \
                for idx in range(len(s)) \
                for rest in self.partition(s[idx+1:]) \
                if s[:idx + 1] == s[:idx + 1][::-1]] or [[]]

# 12 feb, 2019
        return [[s[:i+1] ] + rest\
                 for i in range(len(s))\
                 if s[:i+1] == s[i::-1] \
                for rest in self.partition(s[i+1:])] or [[]]

# dec 17
        res = [[s[:i]] + rest \
               for i in range(1,len(s)+1)  if s[:i]==s[i-1::-1]\
               for rest in self.partition(s[i:])]
        return res or [[]]

    '''