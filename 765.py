# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:47:11 2021

@author: Richard
"""

class Solution:
    def minSwapsCouples(self, row: List[int]) -> int:
        def couple(num):
            if num%2 == 0:
                return num+1
            else:
                return num-1
        def neighbour(i):
            if i%2 == 0:
                return i+1
            else:
                return i-1
        def dfs(i):
            visited[i] = True
            if row[i]==loop_end:
                return
            if visited[neighbour(i)] == False:
                dfs(neighbour(i))
            else:
                dfs(num_to_index[couple(row[i])])
                
        num_to_index = {num:i for i,num in enumerate(row)}
        loops = 0
        visited = [False]*len(row)
        for i,num in enumerate(row):
            if not visited[i]:
                loops += 1
                loop_end = couple(num)
                dfs(i)
        return len(row)//2 - loops