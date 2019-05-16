# -*- coding: utf-8 -*-
"""
Created on Wed May  8 05:07:27 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

i=int(input("enter a number"))
for n in range(i):
    print("*" * n)
for n in range(i):
    a=i-n
    print("*"*a)
    