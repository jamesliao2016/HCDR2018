#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dictn = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}
        if len(digits)==1:
            return dictn[digits[-1]]
        # lst = list(digits)
        prev = dictn[digits[-1]]
        return [i+j for i in self.letterCombinations(digits[:-1]) for j in prev]

if __name__ == '__main__':
    data_ipt = '23'
    dt_opt = Solution()
    print(dt_opt.letterCombinations(data_ipt))

    '''
    Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

    DEC 25
            dictn = {'2':['a','b','c'],
                 '3':['d','e','f'],
                 '4':['g','h','i'],
                 '5':['j','k','l'],
                '6':['m','n','o'],
                '7':['p','q','r','s'],
                '8':['t','u','v'],
                '9':['w','x','y','z']}

        if len(digits)==0:
            return ''
        if len(digits)==1:
            return [i for i in dictn[digits[0]]]
        val_prev = self.letterCombinations(digits[:-1])
        val_add = digits[-1]
        res = [i+j for i in val_prev for j in dictn[val_add] ]

        return res

    '''
