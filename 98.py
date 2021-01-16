# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:39:57 2021

@author: Richard
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    """
    @param root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        return self.isValidBST_helper(root)
    def isValidBST_helper(self, root, low_range = - float('inf'), high_range = float('inf')):
        if not root:
            return True
        elif not (low_range < root.val < high_range):
            return False
        return self.isValidBST_helper(root.left, low_range, root.val)  and self.isValidBST_helper(root.right, root.val, high_range)