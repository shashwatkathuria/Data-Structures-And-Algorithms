# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 20:00:56 2018

@author: shash
"""
import random
graph=[]
reversegraph=[]
file=open("SCC.txt",'r')
for line in file.readlines():
    line=line[:len(line)-2]
    edge1=line.split(" ")
    edge=[int(edge1[0]),int(edge1[1])]
  #  edge2=line.split(" ")
    graph.append(edge)
#    edge2.reverse()
#    reversegraph.append(edge2)
#t=0
#s=0
dictgraph={}
#dictreversegraph={}

for edge in graph:
    tail=edge[0]
    head=edge[1]
    try:
        dictgraph[tail].append(head)
    except:
        dictgraph[tail]=[]
        dictgraph[tail].append(False)
        dictgraph[tail].append(head)
#for edgelist in reversegraph:
#    tail=edgelist[0]
#    head=edgelist[1]
#    try:
#        dictreversegraph[tail].append(head)
#    except:
#        dictreversegraph[tail]=[]

    