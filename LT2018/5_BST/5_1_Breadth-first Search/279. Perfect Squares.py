#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        lst = [n]
        while lst:
            res += 1

            for n in lst:
                tmp = []
                i = 1
                while i*i<=n:
                    if i*i==n:
                        return res
                    tmp.append(n - i*i)
                    i+=1
            lst = tmp

if __name__ == '__main__':
    ipt = 12
    # ipt = 13
    print(Solution().numSquares(ipt))

    '''
    Given a positive integer n, find the least number of perfect square numbers 
    (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

# 19 mar, 2019
        res = 0
        listN = [n]
        while listN:
            res += 1
            tmp = []
            for i in listN:
                j=1
                while j*j<=i:
                    tmp.append(i - j*j)
                    if i - j*j ==0:
                        return res
                    j+=1
            listN = tmp


# 6 jan, 2019
        level = [n]
        res = 0
        while level:
            res += 1
            tmp = []
            for i in level:
                j = 1
                while j*j<=i:
                    tmp.append(i-j*j)
                    if i == j*j:
                        return res
                    j+=1
            level = list(set(tmp))
            # print(level)


# 5 jan, 2019
        if n==0:
            return 0
        res = 0
        i = 1
        lst = []
        while i*i<=n:
            lst.append(i*i)
            i += 1
        nn = {n}
        while nn:
            res += 1
            tmp = set()
            for i in nn:

                for j in lst:
                    if i==j:
                        return res
                    if i<j:
                        break
                    else:
                        tmp.add(i-j)
            nn = tmp

# 12 dec 

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
    '''