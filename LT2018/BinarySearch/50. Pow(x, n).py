#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        print(n)
        if not n:
            return 1
        if n<0:
            return self.myPow(1/x,-n)
        if n %2:
            return x*self.myPow(x,n-1)
        return self.myPow(x*x,n/2)

if __name__ == '__main__':
    x1=2.1
    x2=-5
    output_y=Solution()
    print(output_y.myPow(x1,x2))