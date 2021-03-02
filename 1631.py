# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 10:44:37 2021

@author: Richard
"""
#can't DP because can go from any directions
#<1> modified dijkstra
from collections import defaultdict
import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        heap = []
        heapq.heappush(heap, (0,0,0))
        
        finalized = set()
        score = {(i,j):float("inf") for j in range(n) for i in range(m)}
        # print(score)
        directions = [(0,1),(0,-1),(-1,0),(1,0)]
        while heap:
            effort,x,y = heapq.heappop(heap)
            if (x,y) not in finalized:
                finalized.add((x,y))
                score[(x,y)] = effort
            else:
                continue
            for dx, dy in directions:
                new_x = x+dx
                new_y = y+dy
                if not(0<=new_x<m and 0<=new_y<n):
                    continue
                if (new_x,new_y) in finalized:
                    continue
                new_score = max(score[(x,y)], abs(heights[x][y]-heights[new_x][new_y]))
                if new_score < score[(new_x,new_y)]:
                    heapq.heappush(heap,(new_score,new_x,new_y)) 
        return score[(m-1,n-1)]
    
#<2> binary search + DFS