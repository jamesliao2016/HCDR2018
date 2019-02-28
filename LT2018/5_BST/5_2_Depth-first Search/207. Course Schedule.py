#!/usr/bin/env python2
# coding:utf-8
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        visit = [0] * numCourses
        must = [[]]*numCourses
        for i in prerequisites:
            must[i[0]] = must[i[0]] + i[1:]
        # print(must)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in must[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


if __name__ == '__main__':

    cn = 2; ipt = [[1,0],[0,1]]
    # cn = 2; ipt = [[1,0]]
    # cn = 2;    ipt = [[0, 1]]
    # cn = 3; ipt = [[1, 0], [2, 1]]
    # cn = 3;ipt = [[0,1],[0,2],[1,0]]
    # cn = 3;    ipt = [[0, 1], [0, 2], [1, 2]]
    # cn = 3;    ipt = [[1, 0], [0, 1], [1, 2]]
    print(Solution().canFinish(cn,ipt))

    '''
    There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

# 26 feb, 2019
        visit = [0]*numCourses
        must = [[]]*numCourses
        for i in prerequisites:
            must[i[0]]=must[i[0]]+i[1:]
        print(must)
        def checkFinish(i):
            if visit[i] == -1:
                return False
            if visit[1] == 1:
                return True
            visit[i] = -1
            for j in must[i]:
                if not checkFinish(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not checkFinish(i):
                return False
        return True


# 22 feb, 2019
        visit = [0]*numCourses
        must = [[]] * numCourses
        for i in prerequisites:
            # print(i)
            j = i[0]
            must[j] = must[j] + i[1:]

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in must[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

# 3 jan, 2019
        visit = [0] * numCourses
        must = [[]] * numCourses
        for i in prerequisites:
            tmp = i[0]
            tmp1 = i[1:]
            must[tmp]=must[tmp]+tmp1
        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            if not must[i]:
                visit[i] = 1
                return True
            visit[i] = -1
            for j in must[i]:
                if not dfs(j):
                    return False
            visit[i]=1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        
# 2 jan, 2019
        visit  = [0] * numCourses
        must = [[]] * numCourses
        for i in prerequisites:
            must[i[0]]= must[i[0]] + i[1:]
        # print(must)
        def dfs(i):
            if visit[i] == -1:
                return False
            if not must[i]:
                # visit[i] == 1
                return True
            if visit[i] == 1:
                return True
            visit[i] = -1
            tmp = must[i]
            for j in tmp:
                if not dfs(j):
                    return False
            visit[i]=1
            return True

        for i in range(numCourses):
            if  dfs(i) is False:
                return False
        return True


# 1 jan, 2019
        visit = [0 for _ in range(len(numCourses))]
        graph = [[] for _ in range(len(numCourses))]
        for x,y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for j in graph[i]:
                if not dfs(j):
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    '''