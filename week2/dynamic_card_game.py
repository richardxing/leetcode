# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 14:26:22 2021

@author: Richard
"""

def expected_payoff_card_game(black_total,red_total):
    epo = [[None for _ in range(red_total+1)] for _ in range(black_total+1)]
    for i in range(black_total+1):
        epo[i][0] = i
    for i in range(red_total+1):
        epo[0][i] = 0
    for i in range(1,black_total+1):
        for j in range(1,red_total+1):
            epo[i][j] = max(i/(i+j)*epo[i-1][j]+j/(i+j)*epo[i][j-1],i-j)
    return epo[black_total][red_total]

black_total = 26
red_total = 26
print(expected_payoff_card_game(black_total,red_total))
