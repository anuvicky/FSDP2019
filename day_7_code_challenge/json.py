# -*- coding: utf-8 -*-
"""
Created on Tue May 14 05:31:21 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Jaipur"
url3 = "&appid=948b0c4ed5d456653eb6304da71bb8a3"

url = url1 + url2 + url3
print (url)
response = requests.get(url)
details=response.json()
print(details)
#Latitude_and_Longitude =details["coord"]['lon']['lat']
Weather_Condition=details["main"]["temp_min"]
Wind_Speed=details["wind"]["speed"]
Sunset_Rise_and_Set_timing = details['sys']['sunrise']
#print(Latitude_and_Longitude )
print(Weather_Condition)
print(Sunset_Rise_and_Set_timing)
print(Sunset_Rise_and_Set_timing)