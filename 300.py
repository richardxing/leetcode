# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 20:42:53 2021

@author: Richard
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i]>nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
    
#ending with, transform and conquer, DP, use all previous, if larger-> 续上, 打擂台， O(N^2)