#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for i in set(s):
            if s.count(i)<k:
                return max([self.longestSubstring(tmp,k) for tmp in s.split(i)])
        return len(s)

if __name__ == '__main__':
    s = "aaabb"; k = 3
    # s = "ababbc"; k = 2
    print(Solution().longestSubstring(s,k))

    '''
    Find the length of the longest substring T of a given string 
    (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.

# 11 apr, 2019
        for i in set(s):
            if s.count(i)<k:
                return max([self.longestSubstring(j,k) for j in s.split(i)])
        return len(s)

# 10 apr, 2019
        for i in list(set(s)):
            if s.count(i)<k:
                return max([self.longestSubstring(j,k) for j in s.split(i)])
        return len(s)

# 28 mar, 2019

        lst = list(set(s))
        for i in lst:
            if s.count(i)<k:
                return max(self.longestSubstring(j,k) for j in s.split(i))
        return len(s)

# 27 mar, 2019
        lst = list(set(s))
        for i in lst:
            if s.count(i)<k:
                return max(self.longestSubstring(t,k) for t in s.split(i))
        return len(s)

    '''