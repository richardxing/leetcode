# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 00:14:14 2021

@author: Richard
"""
#did in 2021
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return  nums[0]
        min_ending = nums[0]
        max_ending = nums[0]
        result = max_ending
        for i in range(1,len(nums)):
            min_ending,max_ending = min(nums[i],min_ending*nums[i],max_ending*nums[i]),max(nums[i],max_ending*nums[i],min_ending*nums[i])
            result = max(result,min_ending,max_ending)
        return result
    
#did in 2018
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def product(list):
            p = 1
            for i in list:
                p *= i
            return p
        def maxProduct_no_zero(array):
            if len(array) == 1:
                return array[0]
            pon = []
            for i, num in enumerate(array):
                if num < 0:
                    pon.append(i)
            if len(pon) % 2 == 0:
                return product(array)
            else:
                maxi = -float('inf')
                if pon[0] != len(array)-1:
                    maxi = max(maxi, product(array[pon[0]+1:len(array)]) )
                if pon[-1] != 0:
                    maxi = max(maxi, product(array[0:pon[-1]]))
#                print(pon[0],maxi)
                return maxi
                
            
            
        maxi = -float('inf')
        poz = []
        length = len(nums)
        for i in range(0, length):
            if nums[i] == 0:
                poz.append(i)
        while poz:
            start = poz.pop() + 1
            if start <= length - 1:
                maxi = max(0, maxi, maxProduct_no_zero(nums[start : length]) ) 
                length = start - 1
            else:
                maxi =  max(maxi,0)
                length = start - 1
        print(maxi)
        if length > 0:
            maxi = max(maxi, maxProduct_no_zero(nums[0: length]))
#        print('length:',length)
#        print('maxi_main:', maxi)
#        if maxi == -float('inf'):
#            maxi = 0
        return maxi
