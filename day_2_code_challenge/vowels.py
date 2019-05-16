# -*- coding: utf-8 -*-
"""
Created on Wed May  8 04:49:42 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and while
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'clfrn', 'klhm', 'flrd']
    
"""
state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
for i in state_name:
    #print (i)
    for j in i.lower():
       # print (j)
        for vowels in ['a','e','i','o','u']:
            #print (vowels)
            if j in vowels:
                i=i.replace(j,"")
                print(i)
                
    
        
            
    
    
