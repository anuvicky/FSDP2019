# -*- coding: utf-8 -*-
"""
Created on Fri May 10 20:08:20 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
"""
dict2 = {}
input_file = input ("enter the file name")
with open(input_file,"r") as ff:
    read_lines =  ff.readlines()
    number_of_lines = len(read_lines)
    
    
    #print(read_lines) 
    for a in read_lines:
        words = a.split()
        #print (words)
        counter = 0
        for word in words:
            counter = counter +1
            #print (word)
            #print (a)
            #print(type(a))
            dict2[word] = a.count(word)
            character = 0
            for alph in word :
                #print (alph)
                character = character + 1
#calulate the unique words            
print (dict2.keys())
#caluate how many lines in file
print (number_of_lines)

#calucte the total no charcter the prsent in file
print (character)
    
print (counter)
    
        
















