# -*- coding: utf-8 -*-
"""
Created on Tue May  7 04:51:06 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Ride Cost Calculator
  Filename: 
    ridecost_cal.py
  Problem Statement:
    Assume you travel 80 km to and fro in a day. 
    Cost of Diesel per litre is 80 INR 
    Your vehicle Fuel Average is 18 km/litre. 
    Now calculate the cost of driving per day to office. 
  Hint: 
"""    


travel_per_day = 80
cost_of_disel = 80
vechile_fuel_average = 18
get_of_pertol_per_day = travel_per_day / vechile_fuel_average 
print(get_of_pertol_per_day)
cost_of_driving_per_day = get_of_pertol_per_day * cost_of_disel 
print(round(cost_of_driving_per_day))