#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        i = 1
        lst = []
        while i*i<=n:
            lst.append(i*i)
            i+=1
        res = 0
        ss = {n}
        while ss:
            res += 1
            tmp = set()
            for j in ss:

                for i in lst:
                    if i == j:
                        return res
                    if i > j:
                        break
                    tmp.add(j-i)
            ss = tmp
        return res

if __name__ == '__main__':
    ipt = 12
    print(Solution().numSquares(ipt))

    '''
    Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.
    '''