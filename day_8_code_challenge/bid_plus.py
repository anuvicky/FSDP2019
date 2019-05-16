# -*- coding: utf-8 -*-
"""
Created on Wed May 15 05:58:37 2019

@author: Anupam Sharma
"""

"""
Code Challenge:
  Name: 
    Bid Plus
  Filename: 
    bid_plus.py
  Problem Statement:
      USE SELENIUM
      Write a Python code to Scrap data and download data from given url.
      url = "https://bidplus.gem.gov.in/bidlists"
      Make list and append given data:
          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
     Make a csv file add all data in it.
      csv Name: bid_plus.csv
"""
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup as BS
url = "https://bidplus.gem.gov.in/bidlists"


browser = webdriver.Chrome("C:\\Users\\Anupam Sharma\\Desktop\\chromedriver.exe")
browser.get(url)


sleep(2)

Bid_no =[]
items =[]
quantity =[]
department = []
start_name =[]
end_date=[]
a = browser.find_element_by_xpath('//*[@id="search_concept"]')
for i in range(1,11):
    Bid_no.append('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a')
    items.append('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span)
    quantity.append(//*[@id="pagi_content"]/div[1]/div[2]/p[2]/span)
    start_name.append(//*[@id="pagi_content"]/div[2]/div[4]/p[1]/span)
    end_date.append(//*[@id="pagi_content"]/div[1]/div[4]/p[2]/span)
    
