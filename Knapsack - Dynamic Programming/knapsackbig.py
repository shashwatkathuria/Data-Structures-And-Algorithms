# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:17:15 2018

@author: shash
"""

file=open("BigKnapsack.txt","r")
s=file.readline()
t=s.split(" ")
t=[int(t[0]),int(t[1])]
noofitems=t[1]
capacity=t[0]
weights=[]
values=[]
for i in range(noofitems):
    t=file.readline().split(" ")
    weights.append(int(t[1]))
    values.append(int(t[0]))
ans={}

def knapsack(ans,size,noofitems):
  #  print(noofitems)
    if noofitems==0 or size==0:
        return 0
    
    
    if (noofitems,size) in ans:
        return ans[(noofitems,size)]
    
    if size < weights[noofitems-1]:
        t=knapsack(ans,size,noofitems-1)
    else:
        t=max(knapsack(ans,size,noofitems-1),
              knapsack(ans, size-weights[noofitems-1], noofitems-1)+ values[noofitems-1] )
    ans[(noofitems,size)]=t
    return t

import sys
sys.setrecursionlimit(10000)
#print(ans)
print(knapsack(ans,capacity,noofitems))