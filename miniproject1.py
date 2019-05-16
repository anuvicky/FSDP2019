# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:00:08 2019

@author: Anupam Sharma
"""

import random
while True:
    i=6
    while (i > 0):
        r1=random.randint(0,10)
        i1=int(input("enter a number 1 to 10"))
        if( r1 == i1) :
            print ("players wins")
            break
        else:
            print("player lose")
            print ("secret number {},your guess no {}.".format(r1,i1))    
        i = i-1
        print("the no of tires left")
        print(i)
    print ("if you want to continue  a game type Yes or No ")
    i=bool(input("enter a choice "))
    if(i == False) :
        break
    else :
        continue