# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 19:16:09 2018

@author: shash
"""

file=open("JOBS.txt","r")
size=int(file.readline())
jobs=[]
for i in range(size):
    t=(file.readline()).split(" ")
    t=(int(t[0]),int(t[1]))
    if int(t[0])==100:
       print(t)
    jobs.append(t)
jobs.sort()
jobs.reverse()
mainjobs=[]

#for job in jobs:
#    mainjobs.append((job[0]-job[1],job[1],job[0]))
    
for job in jobs:
    mainjobs.append((job[0]/job[1],job[1],job[0]))
    
mainjobs.sort()

mainjobs.reverse()
t=0
sum=0
for job in mainjobs:
    t=(t+job[1])
    sum+=t*job[2]