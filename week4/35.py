# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:06:16 2021

@author: Richard
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        #same as bisect_left
        if len(nums) == 0:
            return 0
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right-left) //2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:#nums[mid]==target
                return mid
        return left
