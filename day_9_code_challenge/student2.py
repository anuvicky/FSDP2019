# -*- coding: utf-8 -*-
"""
Created on Thu May 16 06:13:42 2019

@author: Anupam Sharma
"""

import mysql.connector 
from pandas import DataFrame

# connect to  MySQL server along with Database name

conn = mysql.connector.connect(user='anupams', password='anupamwinner',
                              host='db4free.net', database = 'student_21')
#, database = 'forsk_test'

# creating cursor
c = conn.cursor()

c.execute("""CREATE TABLE student(
        student_name TEXT,
        student_age INTEGER,
        student_roll_no TEXT,
        student_branch TEXT
        )""")
c.execute("INSERT INTO student VALUES ('anupam',21,'12a','cse')")
c.execute("INSERT INTO student VALUES ('digv',22,'1v6','cse')")
c.execute("INSERT INTO student VALUES ('hrshit',23,'23e','cse')")
c.execute("INSERT INTO student VALUES ('atul',20,'12s','cse')")
c.execute("INSERT INTO student VALUES ('sourab',19,'12d','cse')")
c.execute("INSERT INTO student VALUES ('tapaan',03,'12g','cse')")
c.execute("INSERT INTO student VALUES ('vijay',11,'12h','cse')")
c.execute("INSERT INTO student VALUES ('vikas',99,'12j','cse')")
c.execute("INSERT INTO student VALUES ('khusboo',09,'12k','cse')")
c.execute("INSERT INTO student VALUES ('mohit',00,'12l','cse')")
c.execute("INSERT INTO student VALUES ('sonu',86,'12n','cse')")
c.execute("SELECT * FROM student")
df = DataFrame(c.fetchall())
df.columns =["student_name","student_age","student_roll_no","student_branch"]
conn.commit()
conn.close()
