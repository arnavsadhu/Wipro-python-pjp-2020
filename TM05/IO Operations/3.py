# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 02:25:55 2020

@author: Arnav
"""

z=input('write content to add to test.txt:')
f1=open('test.txt','a')
f1.write(z)
f1.close()