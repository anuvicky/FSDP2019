# -*- coding: utf-8 -*-
"""
Created on Fri May 10 05:05:00 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Zoo Management
  Filename: 
    zoo.py
  Problem Statement:
    Create different functions to :
    read the zoo.csv file using readlines and print them
    Print in list of animals in groups (elephant / tiger / lion / zebra / kangaroo)
    print the total number of water need by elephant / tiger / lion / zebra / kangaroo
    print the total number of water needed by all the animals    
"""

dict1 = {}
sets = set()
list1 = []
with open("zoo.csv","rt") as file:
   # print(value)
    for aa in file:
        #print (aa)
        
        #aa.seek(0,0)
        animal=aa.split(",")
        animals =animal[0]
        #print (animals)
        list1.append(animals)
        animal = set(list1)
        animal.discard('animal')
print(animal)
        
        
        #list1(animals)
        
        
        #print (animal)
        #type(animal)
        #print(animal[0])
        #animals= animal.split()
        #print (animals)
        