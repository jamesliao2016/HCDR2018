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
    '''



