# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 13:40:31 2021

@author: Richard
"""

class Solution:
    def countArrangement(self, n: int) -> int:
        def is_valid(num,index):
            if num%index == 0 or index%num == 0:
                return True
            else:
                return False
        #can use lru_cache?
        def backtracking(numbers_left,index):
            nonlocal result
            if index == n+1:
                result += 1
                return
            numbers_left_copy = numbers_left.copy()
            for num in numbers_left_copy:
                if is_valid(num,index):
                    numbers_left.remove(num)
                    backtracking(numbers_left,index+1)
                    numbers_left.add(num)
        
        result = 0
        backtracking(set(range(1,n+1)),1)
        return result
