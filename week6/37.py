# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 20:05:27 2021

@author: Richard
"""

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        set_row = [set() for _ in range(9)]
        set_col = [set() for _ in range(9)]
        set_square = [[set() for _ in range(3)] for _ in range(3)]
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val != '.': 
                    set_row[row].add(val)
                    set_col[col].add(val)
                    set_square[row//3][col//3].add(val)  
        def dfs(row,col):#fills row,col, return True if working, False if not
            if row == 9 and col == 0:
                return True
            val = board[row][col]
            if val != '.':    
                return dfs(row+col//8,(col+1)%9)

            else:
                valid_choices = set([str(i) for i in range(1,10)]).difference(set_row[row].union(set_col[col],set_square[row//3][col//3]))
                if not valid_choices:
                    return False
                for new_val in valid_choices:
                    board[row][col] = new_val
                    set_row[row].add(new_val)
                    set_col[col].add(new_val)
                    set_square[row//3][col//3].add(new_val)
                    if dfs(row+col//8,(col+1)%9):
                        return True
                    else:
                        #undo choice and continue to next valid choice
                        board[row][col] = '.'
                        set_row[row].remove(new_val)
                        set_col[col].remove(new_val)
                        set_square[row//3][col//3].remove(new_val)
        dfs(0,0)
