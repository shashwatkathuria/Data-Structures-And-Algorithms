# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:25:25 2018

@author: shash
"""

file=open("tspheuristic.txt","r")
s=int(file.readline())
noofcities=s
cities={}
for i in range(noofcities):
    s=file.readline().split()
    s=[float(s[1]),float(s[2])]
    cities[i+1]=s[:]
ordering=list(range(2,noofcities+1))

def distbwcities(citya,cityb):
    return (((citya[0]-cityb[0])**2)+((citya[1]-cityb[1])**2))**0.5



def distfromcityi(i,visited,notvisited):
    dist=[]
    for j in notvisited:
           dist.append([distbwcities(cities[i],cities[j]),j])
    dist.sort()
    return dist[0]

visited=[1]
notvisited=list(range(2,noofcities+1))
def tspheuristic():
    s1=0
    for k in range(1,noofcities):
        
        vertex=visited[-1]
        [distanceneeded,destination]=distfromcityi(vertex,visited,notvisited)
        s1+=distanceneeded
        visited.append(destination)
        notvisited.remove(destination)
        print(destination)
    print(s1+distbwcities(cities[1],cities[visited[-1]]))
#ans=1203406.5012708856
#def tspheuristic():
#    s1=0
#    i=1
#    while len(visited)!=noofcities:
#       print(len(visited))
#       s1+=distbwcities(cities[i],cities[i+1]) 
#       visited.append(i)
#    print(s1+distbwcities(cities[33708],cities[1]))
tspheuristic()
    

