# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 02:38:17 2020

@author: Arnav
"""


f1=open('test.txt','r')
words= f1.read().split()
maxl = len(max(words, key=len))
print( "largest word is:",[word for word in words if len(word) == maxl])
f1.close()