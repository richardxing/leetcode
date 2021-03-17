# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:38:30 2020

@author: Richard
"""
from typing import List
import time

#backtracking, path is a list
class Solution():
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def dfs(path,left,right,n):
            if left == n and right == n:
                result.append("".join(path))
                return
            if left > right:
                path.append(")")
                dfs(path,left,right+1,n)
                path.pop()
            if left < n:
                path.append("(")
                dfs(path,left+1,right,n)
                path.pop()
        
        dfs([], 0, 0, n)
        return result
#
#backtracking, path is a string
s = time.time()
class Solution():
    def generateParenthesis(self, n):
        result = []
        def dfs(s, left, right, n):
            if len(s) == 2 * n:
                result.append(s)
                return
            if left < n:
                dfs(s+'(', left+1, right) #easier handling backtracking with string
            if right < left:
                dfs(s+')', left, right+1)
        dfs("",0,0,n)
        return result
    
obj = Solution()
res = obj.generateParenthesis(16)#17 memory error
print(time.time()-s)


            
#dynamic programming, best solution, 10 lines
s = time.time()
class Solution():
    def generateParenthesis(self, n: int) -> List[str]:
		# Initialize the history list
        seen = [[] for _ in range(n + 1)]
        seen[0].append("")
        if n == 0: 
            return [""]
		
		# Generate the history from 1 pair case
        for total in range(1, n + 1):
			# num_left is the number of pairs in left part
            for num_left in range(total):
				# Iterate through all the possible cases for left and right
                for left in seen[num_left]:
                    for right in seen[total - 1 - num_left]:
                        seen[total].append('(' + left + ')' + right)#essense is this!
        return seen[-1]
obj = Solution()
res = obj.generateParenthesis(17)
print(time.time()-s)



#from itertools import product
#list(product(["("],["()()","(())"],[")"],[""]))

#2021 D&C solution
from functools import lru_cache
class Solution:
    @lru_cache
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(n):
            if n == 0:
                return [""]
            if n == 1:
                return ["()"]
            result = []
            if n > 1:
                for i in range(n):
                    j = n - 1 - i
                    lefts = helper(i)
                    rights = helper(j)
                    for left in lefts:
                        for right in rights:
                            result.append("("+left+")"+right)
            return result
        return helper(n)
    
#2021 backtracking, helper function visit the node, and do other stuffs
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(root,left_used,right_used):
            path.append(root)
            if root == '(':
                #left parens used up to this level
                left_used += 1
            if root == ')':
                #right parens used up to this level
                right_used += 1
            #check if not valid, return
            if right_used>left_used or left_used>n:
                path.pop()
                return
            if left_used==n and right_used == n:
                result.append(''.join(path))
                path.pop()
                return
            helper('(',left_used,right_used)
            helper(')',left_used,right_used)
            path.pop()
            return
        result = []
        path = []
        helper('(',0,0)
        return result
