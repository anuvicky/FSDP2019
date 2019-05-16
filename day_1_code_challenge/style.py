# -*- coding: utf-8 -*-
"""
Created on Tue May  7 05:50:24 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""

a = input("enter a name") #taking a character form user
str1 = a.lower() #convert into a lower a case
str2 = a.upper() #convert into a upper case
str3 = a.title()
print (str1)
print (str2)
print  (str3)