#!/usr/bin/env python2
# coding:utf-8

'''

Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict_par = {'(':')','{':'}','[':']'}
        list_s = list(s)
        list_tmp = []
        while list_s:
            tmp = list_s.pop()
            if tmp not in dict_par:
                list_tmp.append(tmp)
            else:
                if len(list_tmp)>0 and list_tmp[-1] == dict_par[tmp]:
                    list_tmp.pop()
                else:
                    return False
        return True if len(list_tmp)==0 else False

if __name__ == '__main__':
    dt_ipt = "()"
    # dt_ipt = "()[]{}"
    dt_opt = Solution()
    print(dt_opt.isValid(dt_ipt))