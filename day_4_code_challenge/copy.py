# -*- coding: utf-8 -*-
"""
Created on Fri May 10 03:58:43 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""
with open ("romeo.txt","rt") as rf :
    with open ("anupam.txt","w") as wf:
        for line in rf:
            wf.write(line)
