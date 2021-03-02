# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 12:52:33 2021

@author: Richard
"""

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        if m == 0:
            return 0
        def setBitNumber(n):
            # To find the position of the most significant bit
            k = int(math.log(n, 2))
            return 1 << k
        def power_of(num):
            power_num = 0
            while num>1:
                num = num>>1
                power_num += 1
            return 1 << power_num
        most_sig_m = power_of(m)# or call setBitNumber
        most_sig_n = power_of(n)
        if most_sig_m != most_sig_n:
            return 0
        return most_sig_m + self.rangeBitwiseAnd(m-most_sig_m,n-most_sig_n)