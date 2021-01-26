# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 21:20:40 2021

@author: Richard
"""

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total//2

        dp = [[False for _ in range(target+1)] for _ in range(len(nums))]
        if max(nums)>target:#to avoid index overflow for below
            return False
        for i in range(len(nums)):
            dp[i][0] = True
        #base case
        dp[0][nums[0]] = True
        for i in range(1,len(nums)):
            for j in range(target+1):
                if nums[i] > j:#to avoid index overflow for below
                    dp[i][j] = dp[i-1][j]
                else:  
                    dp[i][j] = dp[i-1][j-nums[i]] | dp[i-1][j]
        return dp[len(nums)-1][target]