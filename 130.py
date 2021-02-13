# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 14:26:35 2021

@author: Richard
"""

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        def dfs(node):
#            if node in visited:#should't ever see this line
#                print("shouldn't see this")
#                return
            visited.add(node)#对 就在这里操作
            x,y = node[0],node[1]
            board[x][y] = 'T'#对 就在这里操作
            for dx,dy in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0<= x + dx< m and 0<=y + dy< n and (x+dx,y+dy) not in visited and board[x+dx][y+dy]=='O':#不要漏了条件
                    dfs((x+dx,y+dy))            
        m = len(board)
        n = len(board[0])
        visited=set()
        edge_of_board = set([(0,i) for i in range(n)]).union(set([(m-1,i) for i in range(n)]),set([(i,0) for i in range(m)]),set([(i,n-1) for i in range(m)]))
        for x,y in edge_of_board:#every node as source, do dfs
            if (x,y) not in visited and board[x][y] == 'O':
                dfs((x,y))#除了dfs什么都不要干
        for x in range(m):
            for y in range(n):
                if board[x][y]=='O':
                    board[x][y] = 'X'
                elif board[x][y] == 'T':
                    board[x][y] = 'O'