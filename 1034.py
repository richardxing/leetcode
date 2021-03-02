# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:04:34 2021

@author: Richard
"""

class Solution:
    def colorBorder(self, grid: List[List[int]], r0: int, c0: int, color: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        orig_color = grid[r0][c0]
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        def dfs(r,c):
            visited[r][c] = True
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if not(0<=new_r<m and 0<=new_c<n) or (grid[new_r][new_c] not in [grid[r][c],0]):#replacable to orig_color
                    grid[r][c] = 0
                    break
            for dr, dc in directions:
                new_r, new_c = r+dr, c+dc
                if (0<=new_r<m and 0<=new_c<n) and not visited[new_r][new_c] and grid[new_r][new_c] == orig_color:
                    dfs(new_r,new_c)
        visited = [[False for j in range(n)] for i in range(m)]
        dfs(r0,c0)
        for i in range(m):
            for j in range(n):
                if grid[i][j]==0:
                    grid[i][j] = color
        return grid