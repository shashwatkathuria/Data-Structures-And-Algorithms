# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:22:57 2018

@author: shash
"""
#d={}
#edges=[[1,2,1],[1,3,4],[2,3,2],[2,4,6],[3,4,3]]
#d[1]=[(2,1),(3,4)]
#d[2]=[(3,2),(4,6)]
#d[3]=[(4,3)]
#d[4]=[]
# This program is for a directed graph
file=open("dijkstraData.txt",'r')
edges=[]
for i in range(200):
 s=file.readline()
 s=s[:len(s)-2]
 y=s.split('\t')
 vertex=int(y[0])
 y=y[1:]
 for edge in y:
    t=edge.split(',')
    edges.append([vertex,int(t[0]),int(t[1])])
visited=[1]
notvisited=list(range(2,201,1))
distances=([0]*2)
distances+=[10000]*199
def Dijkstra(edges,vertex):
    minimizethis=[]
    flag=True
    while flag!=False:
      flag=False
      minimizethis=[]
      for edge in edges:
          if (edge[0] in visited) and (edge[1] in notvisited):
            flag=True
            dijkstracriterion=distances[edge[0]]+edge[2]
            minimizethis.append([dijkstracriterion,edge[0],edge[1]])
      if flag==True:
       print(minimizethis)
       minimizethis.sort()
       minimumdijkstra=minimizethis[0]
       distances[minimumdijkstra[2]]=minimumdijkstra[0]
       visited.append(minimumdijkstra[2])
       notvisited.remove(minimumdijkstra[2])
      else:
       return    
Dijkstra(edges,1)        