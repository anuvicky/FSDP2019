# -*- coding: utf-8 -*-
"""
Created on Thu May 16 06:29:40 2019

@author: Anupam Sharma
"""
"""
Code Challenge 3
In the Bid plus Code Challenege 

          1. BID NO
          2. items
          3. Quantity Required
          4. Department Name And Address
          5. Start Date/Time(Enter date and time in different columns)
          6. End Date/Time(Enter date and time in different columns)
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


import mysql.connector 
from pandas import DataFrame

# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='anupams', password='anupamwinner',
                              host='db4free.net', database = 'student_21')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()
c.execute("""CREATE TABLE cricket(
        rank_no INTERGER,
        team TEXT,
        weighted INTERGER,
        rating INTEGER)""")
for i in range(len(rank_no)):
    c.exuete("INSERT INTO cricket VALUES({},{},{},{})".format(rank_no[i],team[i],weighted[i],rating[i]))
    
c.execute("SELECT * FROM cricket")
df = DataFrame(c.fetchall())  # putting the result into Dataframe
df.columns = ["rankno","team","weighted","rating"]
















