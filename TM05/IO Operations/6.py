# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 02:48:46 2020

@author: Arnav
"""


f1=open('test.txt','r')
words= f1.read().split()
z=input("Enter word to get its frequency: ")
f=words.count(z) 
print(f)