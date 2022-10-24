# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 00:27:58 2022

@author: pc
"""

num = int(input("write a number: "))

i = 1
numsum = 0

if num>0:
    while i<=(num//2):
        if num%i==0:
            numsum+=i
        i+=1
        

if num == numsum:
    print("it is a perfect number")
else:
    print("it is not a perfect number")