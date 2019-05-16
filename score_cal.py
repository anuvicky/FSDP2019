# -*- coding: utf-8 -*-
"""
Created on Tue May  7 05:10:40 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""
A1 = int(input("enter the assigments marks 1\n")) #assingments number 1
A2 = int(input("enter the assigments marks 2\n")) #assingments number 2
A3 = int(input("enter the assigments marks 3\n")) #assingments number 3
E1 = int(input("input the exam marks 1\n")) #exam marks 1
E2 = int(input("input the exam marks 2\n")) #exam marks 2
weighted_score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
print(weighted_score) #get the results