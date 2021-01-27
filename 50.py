# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:49:28 2021

@author: Richard
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(x,n):
            if n == 0:
                return 1
            if n < 0:
                return 1/helper(x,-n)
            if n == 1:
                return x
            if n%2 == 0:
                sqrt = helper(x,n//2)
                return sqrt*sqrt
            if n%2 == 1:
                sqrt = helper(x,n//2) 
                return sqrt*sqrt*x
        return helper(x,n)