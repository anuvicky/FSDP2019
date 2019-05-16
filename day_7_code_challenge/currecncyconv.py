# -*- coding: utf-8 -*-
"""
Created on Tue May 14 06:00:57 2019

@author: Anupam Sharma
"""

"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import requests,json
url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=83aef147ab699f9f2e2d"
data = requests.get(url)
a= data.json()
a['USD_INR'] * int(input())