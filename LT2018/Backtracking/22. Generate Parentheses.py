#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def gp(l,r,s='',res=[]):
            if l:
                gp(l-1,r,s+'(',res)
            if l<r:
                gp(l, r-1, s + ')', res)
            if r==0:
                res.append(s)
            return res
        l,r=n,n
        res = []
        gp(l,r,'',res)
        return res

if __name__ == '__main__':
    n = 3
    print(Solution().generateParenthesis(n))

    '''
    Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
    '''