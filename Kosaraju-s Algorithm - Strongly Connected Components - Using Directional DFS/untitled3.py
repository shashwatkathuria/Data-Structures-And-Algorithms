# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:15:10 2018

@author: shash
"""

d={}
t={}
d[1]=[False,4,10]
d[2]=[False,8]
d[3]=[False,6]
d[4]=[False,7]
d[5]=[False,2]
d[6]=[False,9]
d[7]=[False,1]
d[8]=[False,5,6]
d[9]=[False,3,7]
d[10]=[False,4,11]
d[11]=[False,12]
d[12]=[False,10]
time=0
timelash=[0]*13
def DFS(graph,vertex):
     global time
     (graph[vertex])[0]=True
     try:
       neighbours=(graph[vertex])[1:]
     except:
         neighbours=[]
     for neighbour in neighbours:
             if (graph[neighbour])[0]==False:
               try:
                  DFS(graph,neighbour)
               except:
                   print("JINGALLALAH")
     time+=1
     timelash[vertex]=time
     if neighbours==[] :
         return

DFS(d,2)
i=1
order=[]
for key in d:
    print("Timelash for {} is {} ".format(key,timelash[i]))
    order.append((timelash[i],key))
    i+=1 
print(order)
order.sort()
print(order)
timelash=[0]*13

d[1]=[False,7]
d[2]=[False,5]
d[3]=[False,9]
d[4]=[False,1,10]
d[5]=[False,8]
d[6]=[False,3,8]
d[7]=[False,4,9]
d[8]=[False,2]
d[9]=[False,6]  
d[10]=[False,1,12]  
d[11]=[False,10]
d[12]=[False,11]
for o in order:
    timelash=[0]*13
    if d[o[1]][0]==False:
       DFS(d,o[1])
       q=len(timelash)-timelash.count(0)
       print(q)
