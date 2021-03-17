# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 00:21:49 2021

@author: Richard
"""

from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
        heap = []
        heapq.heappush(heap, (0,k))
        
        visited = set()
        score = {i: float('inf') for i in range(1,n+1)}
        while heap:
            delay_time,node = heapq.heappop(heap)
            if node not in visited:
                visited.add(node)
                score[node] = delay_time
            else:
                continue
            for neighbor,travel_time in graph[node]:
                if neighbor in visited:
                    continue
                new_score = travel_time + score[node]
                if new_score < score[neighbor]:
                    heapq.heappush(heap,(new_score,neighbor))
        result = max(score.values())
        if result != float("inf"):
            return result
        else:
            return -1
