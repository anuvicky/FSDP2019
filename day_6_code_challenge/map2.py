# -*- coding: utf-8 -*-
"""
Created on Mon May 13 06:29:30 2019

@author: Anupam Sharma
"""

names = ['Mary', 'Isla', 'Sam']
list_name = list(map(lambda x :hash(x),names))
print (list_name)