# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 20:56:13 2018

@author: shash
"""

file=open("MWIS.txt","r")
s=int(file.readline())
weights={}
for i in range(s):
    weights[i+1]=int(file.readline())
ans=[0]*1001
ans[1]=weights[1]
for i in range(2,1001):
    a1=ans[i-1]
    a2=ans[i-2]+weights[i]
    if a1>a2:
        ans[i]=a1
    else:
        ans[i]=a2
w=[]    
i=1000
while i>0:
   if i!=1:
     a1=ans[i-1]
     a2=ans[i-2]+weights[i]
     print (a1,a2)
     if a2>a1:
        w.append(i)
        i=i-2
     else:
        i=i-1
   if i==1:
      w.append(i)
      i=i-1
      
      
    