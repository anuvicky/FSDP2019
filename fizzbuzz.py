# -*- coding: utf-8 -*-
"""
Created on Tue May  7 10:35:39 2019

@author: Anupam Sharma
"""

"""

Code Challenge
  Name: 
    Fizz Buzz
  Filename: 
    fizzbuzz.py
  Problem Statement:
    Write a Python program which iterates the integers from 1 to 100(included). 
    For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". 
    For numbers which are multiples of both three and five print "FizzBuzz". 
  User Input 
    Not required  
  Output:
    1
    2
    Fizz
    4 
    Buzz  
"""

n=1
#taking input 1 to 100
while (n<101):
    #condition loop chech the condititons
    if( n % 3 == 0 and n % 5 == 0):
        print ("FizzBuzz")
    elif(n % 3 == 0 ):
        print("fizz")
    elif(n % 5 == 0):
        print("BUzz")
    else:
        print(n)
    n = n+1
 
            
            
            
    















