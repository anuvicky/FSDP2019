# -*- coding: utf-8 -*-
"""
Created on Fri May 10 04:32:17 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""
list=[]
with open("kh.txt","w") as aa:
    while True:
        filename = input("enter a student name\n")
        aa.write(filename)
        if not filename :
            break
        list.append(filename)

print(list)      
        