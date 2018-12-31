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
        res = [0] * len(prices)
        for i in range(1,len(prices)):
            res[i] = max(0,prices[i] - prices[i-1]) + res[i-1]
        return res[-1]

if __name__ == '__main__':
    dt_ipt = [7,1,5,3,6,4]
    dt_opt = Solution()
    print(dt_opt.maxProfit(dt_ipt))

'''
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. 
You may complete as many transactions as you like 
(i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time 
(i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.

# dec 30
        res = [0]*len(prices)
        for i in range(1,len(prices)):
            if prices[i]>=prices[i-1]:
                res[i] = res[i-1] +  prices[i] - prices[i-1]
            else:
                res[i] = res[i-1]
        return max(res)


# dec 29

        return sum([max(prices[i+1] - prices[i],0) for i in range(len(prices)-1)])

'''
