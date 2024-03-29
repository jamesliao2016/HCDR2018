#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        if n>0:
            if n%2==0:
                return self.myPow(x*x,int(n/2))
            else:
                return self.myPow(x*x,int(n/2))*x


if __name__ == '__main__':
    # x1=2.1
    # x2=-5
    # x1=1.00001; x2=123456
    x1 = 2;    x2 = 10
    output_y=Solution()
    print(output_y.myPow(x1,x2))

'''
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

# 17 Jan, 2019
        if n==0:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        if n>0:
            if n%2==0:
                return self.myPow(x*x,int(n/2))
            else:
                return self.myPow(x*x,int(n/2))*x

# 16 jan, 2019
        print(n)
        if not n:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        if n %2:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2)

'''