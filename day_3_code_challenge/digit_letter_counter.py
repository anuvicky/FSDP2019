# -*- coding: utf-8 -*-
"""
Created on Thu May  9 22:39:46 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Digit Letter Counter
  Filename: 
    digit_letter_counter.py
  Problem Statement:
    Write a Python program that accepts a string from User and calculate the number of digits and letters.
  Hint:
    Store the letters and Digits as keys in the dictionary  
  Input: 
    Python 3.2
  Output:
    Digits 2
    Letters 6 
"""
digits = {}
letters = {}
alphabet = ['a','b','c','d','e','f','g','h','i','g','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
number = [0,1,2,3,4,5,6,7,8,9]
n=input ("enter a string")
for i in n:
    digits[i] = n.count(int(i))
    letters[i] = n.count(str(i))
print (digits)
print (letters)
            