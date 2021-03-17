# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:16:38 2021

@author: Richard
"""
#<1>sorting, too general, doesn't utilize the [1,n] & containing n + 1 integers constraint
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        previous = 0
        for i in range(len(nums)):
            if nums[i] == previous:
                return previous
            else:
                previous = nums[i]
#O(nlogn)T O(1)S
#<2>hash O(n)T O(n)S
#<3> O(n)T O(1)S? TnC to loop entry&fast slow pointers 
