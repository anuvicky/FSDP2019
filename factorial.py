# -*- coding: utf-8 -*-
"""
Created on Tue May  7 05:26:43 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Facorial
  Filename: 
    factorial.py
  Problem Statement:
    Find the factorial of a number. 
  Hint: 
    Factorial of 3 = 3 * 2 * 1= 6 
    Try to first find the function from math module using dir and help 
  Input:
    Take the number from the keyboard as input from the user.
"""
#how to use specific  function from package or modulues 
from math import factorial 
a = int(input("enter a number")) #taking the input form users
result=factorial(a)
print(result) #get the result