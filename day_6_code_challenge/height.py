# -*- coding: utf-8 -*-
"""
Created on Thu May 16 14:10:10 2019

@author: Anupam Sharma
"""

from functools import reduce

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]

lists = list(map(lambda x :  x['height'],filter( lambda x :'height' in x ,people)))
#print (lists)
if len(lists)>0:
    from operator import add
    average_height = (reduce (add,lists) / len(lists)) 

print (average_height)