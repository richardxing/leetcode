# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 13:50:50 2020

@author: Richard
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        discovered = set()
        counter = 0
        def discover_connected(grid,i,j):
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0<=i+di<len(grid) and 0<=j+dj<len(grid[0]) and grid[i][j] =='1' and (i+di,j+dj) not in discovered:  
                    discovered.add((i+di,j+dj))
                    discover_connected(grid,i+di,j+dj)
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i,j) not in discovered and grid[i][j]=='1':
                    discovered.add((i,j))
                    discover_connected(grid,i,j)
                    counter += 1
        return counter