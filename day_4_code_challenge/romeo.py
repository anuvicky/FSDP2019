# -*- coding: utf-8 -*-
"""
Created on Fri May 10 16:42:20 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""
dict1 = {}

with open("romeo.txt","r") as ff:
    file = ff.readlines()
    print (file)
    #file.split(",")
    for words in file:
        sen=words.split()
        if sen not in dict1:
            dict1[sen] = 1
        else :
            dict1[sen] +=1
print (dict1)
                

       #print (words)
     
           