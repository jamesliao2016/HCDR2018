#!/usr/bin/env python2
# coding:utf-8
'''
来自李航 <<统计学习方法>>第29页的例子
感知机学习算法
'''
class Solution():
    def innerProd(self,x0,x1,w0,w1,b):
        res = w0*x0+w1*x1+b
        return res
    def percept(self,x,y, w0=0, w1=0, b=0):
        res = [0]*len(x)
        for i in range(len(x)):
            tmp = self.innerProd(x[i][0],x[i][1],w0,w1,b)
            res[i] = tmp * y[i]
            if tmp * y[i] <=0:
                w0,w1,b = w0 + x[i][0] * y[i], w1 + x[i][1] * y[i], b+y[i]
                break
        if min(res)>0:
            # return res
            return [w0,w1,b]
        else:
            return self.percept(x,y, w0, w1, b)


if __name__ == '__main__':
    ipt_x = [[3,3],[4,3],[1,1]]
    ipt_y = [1,1,-1]
    print(Solution().percept(ipt_x,ipt_y))
