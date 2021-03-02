# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:29:07 2021

@author: Richard
"""

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result = result^num
        return result