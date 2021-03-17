# -*- coding: utf-8 -*-
"""
Created on Fri Nov 13 18:38:46 2020

@author: Richard
"""
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        q = collections.deque([root])
        res = []
        while q:
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if i==n-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
    
    
