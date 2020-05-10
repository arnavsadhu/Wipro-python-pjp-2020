# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 01:14:23 2020

@author: Arnav
"""

from sys import argv

def checkPrime(n): 
    if (n <= 1): 
        return False
    for i in range(2, n): 
        if (n % i == 0): 
            return False
    return True


s=0

for z in range (1,11):
   if (checkPrime(int(argv[z]))):
       s+=int(argv[z])

print("sum: ",s)
