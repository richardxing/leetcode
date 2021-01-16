# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:02:56 2021

@author: Richard
"""

class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        mapping = {(0,0):0,(0,1):1,(1,0):1,(1,1):0}
        def helper(row,col):
            if row == 1 and col == 1:
                return 0
            res = mapping[(helper(row-1,ceil(col/2)),1-(col%2))]
            return res
        return helper(N,K)