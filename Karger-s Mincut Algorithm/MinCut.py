# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:13:57 2018

@author: shash
"""
import random
n=200
edges=[]
file=open("kargerMinCut.txt","r")
i=0
while i<200:
    
  s=file.readline()
  s=s[0:len(s)-2]
  t=s.split('\t')
  z=t[0]
  for d in t:
      if d!=z:
           edges.append((int(z),int(d)))

  i=i+1
#edges=[(1,2),(1,3),(2,3),(3,4),(2,4),(1,4)]
#n=4
def getvertex(edge):
    if edge[0]>edge[1]:
        return edge[1],edge[0]
    else:
        return edge[0],edge[1]
for edge in edges:
    t=(edge[1],edge[0])
    if t in edges:
        edges.remove(t)


def deletemultipleedges(t):
    for i in range(n**2):
      try:
        edgescopy1.remove(t)
      except:
        break
    for i in range(n**2):
      try:
        edgescopy.remove(t)
      except:
        break
def deleteselfloops():
    temp=edgescopy1[:]
    for edge in temp:
        if edge[0]==edge[1]:
            edgescopy1.remove(edge)

possibilities=[]    

nchoose2=int(n*(n-1)/2)
for k in range(nchoose2):
 print()
 print(k)
 edgescopy=edges[:]
 for i in range(n-2):
  t=random.choice(edgescopy)
  keepthis,removethis=getvertex(t)
#  print(keepthis,removethis)
  edgescopy1=edgescopy[:]
  edgescopy1.remove(t)
  edgescopy.remove(t)
  for edge in edgescopy:
    if removethis in edge:
        for vertex in edge:
            if vertex!=removethis:
                shiftthis=vertex
        edgescopy1.remove(edge)
#        print(edge)
#        print(shiftthis,keepthis,removethis)
        appendthis=(keepthis,shiftthis)
#        print(appendthis)
#        print()
#        print()
        edgescopy1.append(appendthis)
  deleteselfloops()
#  print(edgescopy1)
  edgescopy=edgescopy1[:]
 possibilities.append(len(edgescopy1)) 
# print(min(possibilities),possibilities[-1])

