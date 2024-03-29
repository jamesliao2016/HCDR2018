#!/usr/bin/env python2
# coding:utf-8
# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return []
        val = sorted(intervals,key= lambda x: x[0])
        res = []
        res.append(val[0])
        for i in val:
            if i[0] <= res[-1][1]:
                res[-1][1] = max(i[1],res[-1][1])
                res[-1][0] = min(res[-1][0],i[0])
            else:
                res.append(i)
        return res





if __name__ == '__main__':
    # ipt = [[1,3],[2,6],[8,10],[15,18]]
    ipt=[[1, 4], [2, 3]]
    itv = []
    for i in ipt:
        tmp = Interval(i[0],i[1])
        itv.append(tmp)
    opt = Solution().merge(itv)
    for i in opt:
        print(i.start,i.end)

    '''
    Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

# 11 july, 2019
        val = sorted(intervals,key= lambda x: x.start)
        res = []
        res.append(val[0])
        for i in val:
            if i.start <= res[-1].end:
                res[-1].end = max(res[-1].end,i.end)
            else:
                res.append(i)
        return res

# 19 apr, 2019
        # return intervals.sort(lambda x: x.key=)
        # return sorted(intervals,key= lambda x: x.start)
        # return intervals
        val =  sorted(intervals,key= lambda x: x.start)
        res = []
        for i in range(len(val)):
            if not res or res[-1].end<val[i].start:
                res.append(val[i])
            elif res[-1].end>=val[i].start and res[-1].end<val[i].end:
                res[-1].end = val[i].end
        return res

    '''



