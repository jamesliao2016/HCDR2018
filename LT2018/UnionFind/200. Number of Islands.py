#!/usr/bin/env python2
# coding:utf-8

class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        def dfs(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
                return 0
            grid[i][j] = '#'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            return 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(grid,i,j)
        return res


if __name__ == '__main__':
    ipt = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
    # ipt = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(Solution().numIslands(ipt))

    '''
    Share
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:

Input:
11110
11010
11000
00000

Output: 1
Example 2:

Input:
11000
11000
00100
00011

Output: 3

# 22 feb, 2019
        if not grid:
            return 0
        def dfs(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
                return 0
            grid[i][j]='#'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            return 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(grid,i,j)
        return res


# 21 feb, 2019
        if not grid:
            return 0
        def dfs(grid,i,j):
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
                return 0
            grid[i][j] = '#'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)
            return 1
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += dfs(grid,i,j)
        return res

# Jan 3, 2019
        if not grid:
            return 0
        res = 0
        def dfs(grid,i,j):
            if i<0 or i >=len(grid) or j<0 or j>= len(grid[0]) or grid[i][j]!='1':
                return
            grid[i][j] = '#'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j )
            dfs(grid,i,j+1 )
            dfs(grid,i,j-1 )
            return 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(grid,i,j):
                    res +=1
        return res
        
# Jan 2, 2018
        if not grid:
            return 0
        def dfs(grid,i,j):

            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!='1':
                return
            grid[i][j] = '#'
            dfs(grid,i+1,j)
            dfs(grid,i-1,j)
            dfs(grid,i,j+1)
            dfs(grid,i,j-1)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    dfs(grid,i,j)
        return res


# jan 1, 2019
        def dfs(grid,i,j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j]!='1':
                return
            grid[i][j]='#'
            dfs(grid,i,j+1)
            dfs(grid, i, j - 1)
            dfs(grid, i-1, j)
            dfs(grid, i + 1, j)
        if not grid:
            return 0
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]=='1':
                    res += 1
                    dfs(grid,i,j)
        return res

    '''