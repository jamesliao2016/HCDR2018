#!/usr/bin/env python2
# coding:utf-8


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dicts = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s)-1):
            if dicts[s[i]]>dicts[s[i+1]]:
                res += dicts[s[i]]
            else:
                res -= dicts[s[i]]
        res += dicts[s[-1]]
        return res
if __name__ == '__main__':
    print(Solution().romanToInt('IX'))
'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
'''

'''
dec 24

        dict_n ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        res = 0
        for i in range(len(s)-1):
            val = s[i]
            val2 = s[i+1]
            if dict_n[val] < dict_n[val2]:
                res -= dict_n[val]
            else:
                res += dict_n[val]
        return res + dict_n[s[len(s)-1]]

'''