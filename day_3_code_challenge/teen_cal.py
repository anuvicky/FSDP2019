# -*- coding: utf-8 -*-
"""
Created on Thu May  9 20:19:14 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Teen Calculator
  Filename: 
    teen_cal.py
  Problem Statement:
    Take dictionary as input from user with keys, a b c, with some integer 
    values and print their sum. However, if any of the values is a teen -- 
    in the range 13 to 19 inclusive -- then that value counts as 0, except 
    15 and 16 do not count as a teens. Write a separate helper "def 
    fix_teen(n):"that takes in an int value and returns that value fixed for
    the teen rule. In this way, you avoid repeating the teen code 3 times  
  Input: 
    {"a" : 2, "b" : 15, "c" : 13}
  Output:
    Sum = 17
"""

n = int (input("enter a vlaue"))
sum = 0
d = {}
for n in range(n):
    key = input()
    values = int(input())
    d[key] = values
    if values in 13 or 14 or 17 or 18 or 19:
        continue
    else :
        sum =sum + d[key]
print (d)
print ("sum=")
print()