#!/usr/bin/env python2
# coding:utf-8

'''

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).
'''

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        return sum([max(prices[i+1] - prices[i],0) for i in range(len(prices)-1)])

if __name__ == '__main__':
    dt_ipt = [7,1,5,3,6,4]
    dt_opt = Solution()
    print(dt_opt.maxProfit(dt_ipt))
