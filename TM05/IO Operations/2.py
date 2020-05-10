# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 02:17:05 2020

@author: Arnav
"""

n=int(input("Enter the number lines to print:"))
f1=open('test.txt')
lines=f1.readlines()
for z in range(n):
    print(lines[z])
f1.close()