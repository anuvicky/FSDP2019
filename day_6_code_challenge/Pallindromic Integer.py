# -*- coding: utf-8 -*-
"""
Created on Mon May 13 04:02:10 2019

@author: Anupam Sharma
"""
user_input = input("enter a number").split()
length = len (user_input)
print (length)
for i in range(length):
    if user_input[i] in user_input[i][::-1]:
        continue
    else :
        print (False)
        break   
     
user_input = input("enter a number").split()
user=[int(i) for i in user_input]
list1=[ True if i > 0 and str(i)==str(i)[::-1] else False for i in user]
print(all(list1))
    
