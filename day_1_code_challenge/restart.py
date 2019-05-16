# -*- coding: utf-8 -*-
"""
Created on Tue May  7 06:07:24 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""
a = "RESTART"
f = a.rfind("R")
print(a[:f] + "$" + a[f+1:])

















