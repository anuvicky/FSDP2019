# -*- coding: utf-8 -*-
"""
Created on Wed May 15 04:44:06 2019

@author: Anupam Sharma
"""

from bs4 import BeautifulSoup
import requests
icc = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
cricket = requests.get(icc).text
soup = BeautifulSoup(cricket,"lxml")
all_tables=soup.find_all('table')
right_table=soup.find('table', class_='table')

a =[]
b =[]
c =[]
d =[]
e =[]
for row in right_table.findAll('tr'):
    column = row.findAll('td')
    if len(column) == 5:
        a.append(column[0].text.strip())
        b.append(column[1].text.strip())
        c.append(column[2].text.strip())
        d.append(column[3].text.strip())
        e.append(column[4].text.strip())
import pandas as pd
from collections import OrderedDict

col_name = ["rank_no","team","weighted","points","rating"]
col_data = OrderedDict(zip(col_name,[a,b,c,d,e]))
#print (col_data)
df = pd.DataFrame(col_data) 
print (df)
        

 









    