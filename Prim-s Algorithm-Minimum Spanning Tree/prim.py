# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:28:19 2018

@author: Shashwat Kathuria
"""

file=open("PRIM.txt","r")
t=file.readline().split(" ")
n=int(t[0])
m=int(t[1])
edges=[]
for i in range(m):
    t=file.readline().split(" ")
    edges.append([int(t[0]),int(t[1]),int(t[2])])

visited=[500]
notvisited=list(range(1,500,1))
cost=0
def PRIM(edges):
 #   print(visited)
    global cost
    flag=True
    while flag!=False:
     minimizethis=[]
     flag=False
     for edge in edges:
        if edge[0] in visited and edge[1] in notvisited:
        #    print(edge)
            flag=True
            minimizethis.append((edge[2],edge[0],edge[1]))
        if edge[0] in notvisited and edge[1] in visited:
        #    print(edge)
            flag=True
            minimizethis.append((edge[2],edge[1],edge[0]))
     if flag==True :
      minimizethis.sort()
      edgechosen=minimizethis[0]
      cost+=edgechosen[0]
      visited.append(edgechosen[2])
      notvisited.remove(edgechosen[2])
    return(cost)
print("Minimum Cost Spanning Tree Cost:")
print(PRIM(edges))
    
            
