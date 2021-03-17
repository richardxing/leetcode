# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 13:03:15 2021

@author: Richard
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        bitmap = [0 for _ in range(len(words))]
        for i,word in enumerate(words):
            letters = set(word)
            for letter in letters:
                bitmap[i] |= 1<<(ord(letter) - ord('a'))
        max_product_len = 0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                if bitmap[i] & bitmap[j] == 0:
                    max_product_len = max(max_product_len,len(words[i])*len(words[j]))
        return max_product_len
