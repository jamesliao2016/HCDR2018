#!/usr/bin/env python2
# coding:utf-8
class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 5:
            return 0
        return int(n / 5) + self.trailingZeroes(int(n / 5))
