# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 00:39:30 2021

@author: Richard
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        list0=ListNode(object)
        start=list0
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                list0.next=l1
                list0=list0.next
                l1=l1.next
            else :
                list0.next=l2
                list0=list0.next
                l2=l2.next
        if l1 is None:
            list0.next=l2
        else:
            list0.next=l1
        return start.next