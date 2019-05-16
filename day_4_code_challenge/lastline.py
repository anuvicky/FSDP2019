# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:06:23 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""

text_file = input("enter a text file which you want")
with open(text_file , mode='r') as file:
    last_line = file.readlines()[-1]
    print (last_line)