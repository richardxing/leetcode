# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 12:30:44 2021

@author: Richard
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def helper(root,numbers_remain):
            path.append(root)
            if len(numbers_remain)==0:
                result.append(path[1:].copy())
                path.pop()
                return 

            for i in numbers_remain:
                new_numbers = numbers_remain.copy()
                new_numbers.remove(i)
                helper(i,new_numbers)
            path.pop()
        path = []
        result = []
        numbers_remain = set(nums)
        helper(None,numbers_remain)
        return result
