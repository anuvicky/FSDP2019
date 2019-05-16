# -*- coding: utf-8 -*-
"""
Created on Thu May  9 21:49:42 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""

dict1 = {}
i = input("enter a sentences")
#print (i)
for string in i:
    #print(string)
    dict1[string] = i.count(string)
print(dict1)



