# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 22:24:14 2021

@author: Richard
"""
#<1>easier to write with = 
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def no_elements_se(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:#= important
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if no_elements_se(mid) > k:
                right = mid
            elif no_elements_se(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left
#<2> also works, much harder to write
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        def no_elements_st(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] < mid:#alternatively, no equal sign
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num

        left, right = matrix[0][0], matrix[-1][-1]
        while right - left >= 2:
            mid = (left + right) // 2
            if no_elements_st(mid) > k:
                right = mid - 1
            elif no_elements_st(mid) < k:
                left = mid
            else:
                right = mid
        if no_elements_st(right) >= k:
            return left
        else:
            return right
            