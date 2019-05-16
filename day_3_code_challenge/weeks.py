# -*- coding: utf-8 -*-
"""
Created on Thu May  9 04:11:15 2019

@author: Anupam Sharma
"""


"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""


name_of_days=('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
#print (name_of_days)
i=input("enter a days").split()
#print (i)
#type(i)
for item,value in enumerate(name_of_days):
    print(value)
    if value not in i:
        i.insert(item,value)
 
print(i)


    
        

        
        
        
