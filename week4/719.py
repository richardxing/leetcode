# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 00:34:09 2021

@author: Richard
"""

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def no_pd_se(dist):
            total = 0
            for i in range(len(nums)):
                total+=bisect.bisect_right(nums,nums[i]+dist)-1-i
            return total
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = left+(right-left)//2
            if no_pd_se(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

#earlier stopping, almost the same 
class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        def no_pd_se_mtk(dist):
            total = 0
            for i in range(len(nums)):
                total+=bisect.bisect_right(nums,nums[i]+dist)-1-i
                if total>=k:
                    return True
            return total>=k
        nums.sort()
        left = 0
        right = nums[-1] - nums[0]
        while left < right:
            mid = left+(right-left)//2
            if no_pd_se_mtk(mid):
                right = mid
            else:
                left = mid + 1
        return left
