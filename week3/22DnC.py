# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 18:53:06 2021

@author: Richard
"""

from functools import lru_cache
class Solution:
    @lru_cache
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n):
            if n == 0:
                return [""]
            if n == 1:
                return ["()"]
            result = []
            if n > 1:
                for i in range(n):
                    j = n - 1 - i
                    lefts = helper(i)
                    rights = helper(j)
                    for left in lefts:
                        for right in rights:
                            result.append("("+left+")"+right)
            return result
        return helper(n)
