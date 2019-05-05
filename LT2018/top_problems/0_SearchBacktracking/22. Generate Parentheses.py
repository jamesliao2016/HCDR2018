#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def helper(i,j,tmp='',res=[]):
            if i>0:
                helper(i-1,j,tmp+'(',res)
            if j>0 and j>i:
                helper(i,j-1,tmp+')',res)
            if j==0:
                res.append(tmp)

        res = []
        helper(n,n,'',res)
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

# 3 apr, 2019
        def helper(i,j,tmp='',res=[]):
            if i>0:
                helper(i-1,j,tmp+'(',res)
            if j>0 and j>i:
                helper(i,j-1,tmp+')',res)
            if j==0:
                res.append(tmp)

        res = []
        helper(n,n,'',res)
        return res

# 2 apr, 2019
        def helper(l,r,tmp='',res=[]):
            if l:
                helper(l-1,r,tmp+'(',res)
            if l<r:
                helper(l,r-1,tmp+')',res)
            if not r:
                res.append(tmp)
            return res
        res = []
        helper(n,n,'',res)
        return res

# 11 jan, 2019
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

    '''