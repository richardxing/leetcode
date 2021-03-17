# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:45:00 2021

@author: Richard
"""

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        def helper(node):
            if node is None:
                return 0
            if node.left is not None:
                depth_left = helper(node.left)
            else:
                depth_left = 0 
            if node.right is not None:
                depth_right = helper(node.right)
            else:
                depth_right = 0
            return max(depth_left,depth_right)+1
        return helper(root)
