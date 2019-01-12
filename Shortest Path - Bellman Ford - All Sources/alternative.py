# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 08:14:28 2018

@author: shash
"""
#FOR CHECKING A NEGATIVE CYCLE,JUST CHECK ANY ONE ITERATION,IF FOUND,HALT,IF NOT,THEN UNCOMMENT THE EARLY HALTING FLAG2 LINES TO MAKE THE PROGRAM/ALGORITHM RUN FASTER
#ALL VERTICES SHORTEST PATHS
#d={}
#g3=-19
#g2,g1=negative cycle
#d[1]=[False,2,3]
#d[2]=[False,3,4]
#d[3]=[False,4]
#d[4]=[False]
#
#edges={}
#edges[1,2]=1
#edges[1,3]=3
#edges[2,3]=-7
#edges[3,4]=5
#edges[2,4]=2
#edges[tail,head]=edgecost
file=open("g3.txt","r")
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
minimums=[]
indegreeneighbours={}
    
for vertex in range(1,noofvertices+1):
            indegreeneighbours[vertex]=[]
   #         print(vertex)
            for key in d:
                if vertex in d[key][1:]:
                    indegreeneighbours[vertex].append(key)
    
for source in range(941,noofvertices+1):   
    print(source)
    shortestpaths={}
    
    #noofvertices=4
    noofedges=noofvertices# -1
    

    for k in range(1,noofvertices+1):
        for i in range(0,noofedges+1):
            if source==k:
                shortestpaths[k,i]=0
            else:
                shortestpaths[k,i]=9999999

    for i in range(1,noofedges+1):
   #     print(i)
        flag2=False
        for vertex in range(1,noofvertices+1):
    #        print(vertex)
            path1=shortestpaths[vertex,i-1]
            path2=[]
            for neighbour in indegreeneighbours[vertex]:
                  path2.append(shortestpaths[neighbour,i-1]+edges[neighbour,vertex])
            if path2!=[]:
               minpath2=min(path2)
               shortestpaths[vertex,i]=min(path1,minpath2)
            else:
                shortestpaths[vertex,i]=path1
            if shortestpaths[vertex,i]!=shortestpaths[vertex,i-1]:
                flag2=True
        if flag2==False:
            print("Hello",i)
            break
#    flag=True
#    for key in shortestpaths:
#        if shortestpaths[key[0],noofedges]!=shortestpaths[key[0],noofedges-1]:
#            print("Negative Cycle Present")
#            flag=False
#            break
#    if flag==False:
#        break
#    else:
    x=min(shortestpaths.values())
    print(x)
    minimums.append(x)