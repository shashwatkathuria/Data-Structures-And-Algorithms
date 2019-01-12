# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 07:31:55 2018

@author: shash
"""

#ALL VERTICES SHORTEST PATHS
#d={}
#d[vertex]=[Visited or Not,neighbour1,neighour2,..]
#edges={}
#edges[tail,head]=edgecost
file=open("g1.txt","r")
s=file.readline().split(" ")
s=[int(s[0]),int(s[1])]
noofvertices=s[0]
noofedges1=s[1]

d={}
for vertex in range(1,noofvertices+1):
    d[vertex]=[False]
edges={}
for i in range(noofedges1):
    s=file.readline().split(" ")
    s=[int(s[0]),int(s[1]),int(s[2])]
    edges[s[0],s[1]]=s[2]
    d[s[0]].append(s[1])    
shortestpaths={}

#noofvertices=4
noofedges=noofvertices# -1

indegreeneighbours={}

for vertex in range(1,noofvertices+1):
        indegreeneighbours[vertex]=[]
        print(vertex)
        for key in d:
            if vertex in d[key][1:]:
                indegreeneighbours[vertex].append(key)

for j in range(1,noofvertices+1):
  for k in range(1,noofvertices+1):
    for i in range(0,noofedges+1):
        if j==k:
            shortestpaths[j,k,i]=0
        else:
            shortestpaths[j,k,i]=9999999
for source in range(1,noofvertices+1):
 print(source)
 for i in range(1,noofedges+1):
    print(i)
    for vertex in range(1,noofvertices+1):
        print(vertex)
        path1=shortestpaths[source,vertex,i-1]
        path2=[]
        for neighbour in indegreeneighbours[vertex]:
              path2.append(shortestpaths[source,neighbour,i-1]+edges[neighbour,vertex])
        if path2!=[]:
           minpath2=min(path2)
           shortestpaths[source,vertex,i]=min(path1,minpath2)
        else:
            shortestpaths[source,vertex,i]=path1
for key in shortestpaths:
    if shortestpaths[key[0],key[1],noofedges]!=shortestpaths[key[0],key[1],noofedges-1]:
        print("Negative Cycle Present")
        break
        
        