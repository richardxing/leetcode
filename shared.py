# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 20:04:55 2021

@author: Richard
"""

from collections import Counter
class Solution:
    # def findDuplicate(self, nums: List[int]) -> int:
    #     nums_to_count = Counter(nums)
    #     for num,count in nums_to_count.items():
    #         if count>1:
    #             return num
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        previous = nums[0]
        for i in range(1,len(nums)):
            if nums[i] == previous:
                return previous
            previous = nums[i]



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        def find_first(nums,target):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right-left)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    right = mid
            if left > right:
                return -1
            else:
                return left if nums[left]==target else -1
        
        def find_last(nums, target):
            left = 0
            right = len(nums) - 1
            while left < right:
                mid = left + (right-left+1)//2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid
            if left > right:
                return -1
            else:
                return left if nums[left]==target else -1
        return [find_first(nums,target),find_last(nums,target)]
