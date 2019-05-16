# -*- coding: utf-8 -*-
"""
Created on Tue May  7 06:41:04 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

str1 =  "Welcome to Pink City Jaipur"
str2 = str1.replace(" ","*")
print (str2)