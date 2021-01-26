# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 00:12:37 2021

@author: Richard
"""

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        min_moves = [[None for _ in range(N+1)] for _ in range(K+1)]
        for j in range(N+1):
            min_moves[1][j] = j 
        for i in range(2,K+1):
            for j in range(0,N+1):
                if j == 0:
                    min_moves[i][j]=0
                else:
                    min_moves[i][j] = min(max(1+min_moves[i-1][j-choice_floor],1+min_moves[i][choice_floor-1]) for choice_floor in range(1,j+1))
        print(min_moves)
        return min_moves[K][N]
#O(KN^2) time limit exceeded