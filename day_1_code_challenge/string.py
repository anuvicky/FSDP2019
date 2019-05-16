# -*- coding: utf-8 -*-
"""
Created on Tue May  7 06:31:39 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    string.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""
str1 = "Sylvester Fernandes"
str2 = str1.find(" ")
print(str2)
print (str1[str2:] +" "+str1[:str2])