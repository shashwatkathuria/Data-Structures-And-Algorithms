# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:59:15 2018

@author: shash
"""

file=open("SmallKnapsack.txt","r")
s=file.readline()
t=s.split(" ")
t=[int(t[0]),int(t[1])]
noofitems=t[1]
capacity=t[0]
items={}
for i in range(noofitems):
    t=file.readline().split(" ")
    items[i+1]=[int(t[0]),int(t[1])]

ans={}
for x in range(capacity+1):
    ans[0,x]=0


for i in range(1,noofitems+1):
     print(i)
     for x in range(capacity+1):
         if items[i][1]>x:
             ans[i,x]=ans[i-1,x]
             continue
         a1=ans[i-1,x]
         a2=ans[i-1,x-items[i][1]]+items[i][0]
         if a2>a1:
             ans[i,x]=a2
         else:
             ans[i,x]=a1
         
    
    