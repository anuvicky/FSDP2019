# -*- coding: utf-8 -*-
"""
Created on Thu May  9 03:49:02 2019

@author: Anupam Sharma
"""
"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""

i=input("enter a number")
l=i.split()
y=tuple(l)
print (l)
print (y)
    
