# -*- coding: utf-8 -*-
"""
Использую только переменную S. нерезание (S[1:2]) и конкатенацию (string + string)
выведите переменную  S = slam

"""
S = "spaml"

S = S[0:1] + S[4:0:-2] + S[3:4]

print(S)
