# -*- coding: utf-8 -*-
"""
Created on Thu May 16 15:17:44 2019

@author: Anupam Sharma
"""

lists =[[ "34587", "Learning Python, Mark Lutz" , 4 ,40.95],
    ["98762"," Programming Python, Mark Lutz" ,5, 56.80],
    ["77226"," Head First Python, Paul Barry" ,3, 32.95],
    ["88112"," Einführung in Python3, Bernd Klein"  ,3, 24.99]]
#print(lists[0][3])
order_summary = list(map(lambda x : (x[0],round(x[2] *x[3],x[2])),lists))
print (order_summary)





order_summary=[]
lists =[[ "34587", "Learning Python, Mark Lutz" , 4 ,40.95],
    ["98762"," Programming Python, Mark Lutz" ,5, 56.80],
    ["77226"," Head First Python, Paul Barry" ,3, 32.95],
    ["88112"," Einführung in Python3, Bernd Klein"  ,3, 24.99]]
#print (len(lists))
for i in lists:
    #print(i)
    #print(i[3])
    order_no=i[0]
    quantity=i[2]
    price=i[3]
    total=quantity *price
    if total<=100:
        total +=10
    else :
        total
    order_summary.append((order_no,total))
print(order_summary)    
            
    