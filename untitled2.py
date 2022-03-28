# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 17:02:51 2021

@author: acer
"""

for a in range(0,1001):
    for b in range(a,1001):
        for c in range(b,1001):
            if(a+b+c==1000 and a**2+b**2==c**2):
                x=a*b*c
print(x)