# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 22:33:50 2018

@author: shash
"""
#SINGLE VERTEX SHORTEST PATH
d={}
d[1]=[False,2,3]
d[2]=[False,3,4,5]
d[3]=[False,4,6]
d[4]=[False,5,6]
d[5]=[False]
d[6]=[False]

edges={}
edges[1,2]=-1
edges[1,3]=-4
edges[2,3]=-2
edges[3,4]=5
edges[2,4]=3
edges[2,5]=-8
edges[4,5]=-2
edges[3,6]=10
edges[4,6]=15
#edges[tail,head]=edgecost

shortestpaths={}

noofvertices=6
noofedges=noofvertices-1

indegreeneighbours={}

for vertex in range(1,noofvertices+1):
        indegreeneighbours[vertex]=[]
        print(vertex)
        for key in d:
            if vertex in d[key][1:]:
                indegreeneighbours[vertex].append(key)
sourcevertex=1
for j in range(0,noofedges+1):
    shortestpaths[sourcevertex,j]=0
    
for k in range(2,noofvertices+1):
    for i in range(0,noofedges+1):
       shortestpaths[k,i]=9999999

for i in range(1,noofedges+1):
    print(i)
    for vertex in range(1,noofvertices+1):
        print(vertex)
        path1=shortestpaths[vertex,i-1]
        path2=[]
        for neighbour in indegreeneighbours[vertex]:
              path2.append(shortestpaths[neighbour,i-1]+edges[neighbour,vertex])
        if path2!=[]:
           minpath2=min(path2)
           shortestpaths[vertex,i]=min(path1,minpath2)
        else:
            shortestpaths[vertex,i]=path1
        
        