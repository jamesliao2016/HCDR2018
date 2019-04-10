#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergeSmall(lst,res):
            mid = int(len(lst)/2)
            if mid:
                l,r = mergeSmall(lst[:mid],res),mergeSmall(lst[mid:],res)
                for i in range(len(lst))[::-1]:
                    if not r or (l and l[-1][1]>r[-1][1]):
                        res[l[-1][0]] += len(r)
                        lst[i] = l.pop()
                    else:
                        lst[i] = r.pop()
                return lst
        res = [0]*len(nums)
        mergeSmall(list(enumerate(nums)),res)
        return res


if __name__ == '__main__':
    ipt = [5,2,6,1]
    print(Solution().countSmaller(ipt))

    '''
    You are given an integer array nums and you have to return a new counts array. 
    The counts array has the property where counts[i] is the number of smaller elements to 
    the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.






# 10 apr, 2019
        def mg(lst):
            mid = int(len(lst) / 2)
            if mid:
                l,r = mg(lst[:mid]), mg(lst[mid:])
                for i in range(len(lst))[::-1]:
                    if (not r) or (l and l[-1][1] > r[-1][1]):
                        res[l[-1][0]] += len(r)
                        lst[i] = l.pop()
                    else:
                        lst[i] = r.pop()
            return lst
        res = [0] * len(nums)
        mg(list(enumerate(nums)))
        return res

    '''