# -*- coding: utf-8 -*-
"""
Created on Sat May 11 23:02:37 2019

@author: Anupam Sharma
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

list1= []
import re
while True:
    input_user = input("enter multiple mails")
    if not input_user:
        break
    elif re.match(r'^[\w-]+@[a-zA-z0-9]+\.[a-z]{2,4}$',input_user):
        list1.append(input_user)

print (list1)
        
        
    
            
        






















