# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 14:05:51 2021

@author: Richard
"""

class Solution:
#    def getSum(self, a: int, b: int) -> int:
#        if b == 0:
#            return a
#        print(a,b)
#        temp = a^b
#        pro = (a&b) << 1
#        return self.getSum(temp,pro)
    def getSum(self, a: int, b: int) -> int:
        return sum([a, b])