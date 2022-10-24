# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 00:20:23 2022

@author: pc
"""

#we will write a function for finding perfect number

num = int(input("write a number: "))
num_list = []

if num>0:
    for i in range(1, num//2+1):
        if num%i == 0:
            num_list.append(i)

if num == sum(num_list):
    print("it is a perfect number")
else:
    print("it is not a perfect number")

