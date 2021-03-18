# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:03:05 2021

@author: Richard
"""

class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        def dfs(groups):
            if not nums: #all groups must be equal to target
                return True
            v = nums.pop()
            for i, group in enumerate(groups):
                if group + v <= target:
                    groups[i] += v
                    if dfs(groups): 
                        return True
                    groups[i] -= v
                # if not group: 
                #     break
            nums.append(v)
            return False
        
        target, remainder = divmod(sum(nums), k)
        if remainder: 
            return False
        nums.sort()
        if nums[-1] > target: 
            return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        return dfs([0] * k)
        
    
#    
##incomplete/wrong answers
#from collections import Counter
#class Solution:
#    def canPartitionKSubsets(self, nums, k):
#        total = sum(nums)
#        if  total%k!= 0:
#            return False
#        target = total//k
#        ct = Counter(nums)
#        for i, count in ct.items():#reverse order
#            if i > target:
#                return False
#            if i== target:
#                continue
#            if target - i 
#            
#from collections import Counter
#class Solution:
#    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
#        def dfs(subsets,nums):
#            print(subsets,nums)
#            if not nums:
#                if all(i == target for i in subsets):
#                    return True
#                else:
#                    return False
#            new_el = nums.pop()
#            for i,s in enumerate(subsets):
#                if s+nums[-1] <= target:
#                    subsets[i] += new_el
#                    flag = dfs(subsets,nums)
#                    subsets[i] -= new_el
#                    if flag:
#                        return True
#                    
#            nums.append(new_el)       
#            new_el = nums.pop()
#            subsets.append(new_el)
#            flag = dfs(subsets,nums)
#            nums.append(new_el)
#            subsets.pop(new_el)
#            if flag:
#                return True
#            return False
#        if sum(nums)%k != 0:
#             return False
#        target = sum(nums)//k
#        if any(i>target for i in nums):
#            return False
#        return dfs([],nums)   


         