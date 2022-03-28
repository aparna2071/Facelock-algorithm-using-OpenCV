# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:28:15 2021

@author: acer
"""

sum=0
for num in range(1, 200000):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           sum+=num
print(sum)
