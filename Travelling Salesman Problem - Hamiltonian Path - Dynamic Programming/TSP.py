# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:06:39 2018

@author: shash
"""
import time
start=time.time()
file=open("TSP.txt","r")
s=int(file.readline())
noofcities=s
cities={}
for i in range(noofcities):
    s=file.readline().split()
    s=[float(s[0]),float(s[1])]
    cities[i+1]=s[:]
ordering=list(range(2,noofcities+1))

def distbwcities(citya,cityb):
    return (((citya[0]-cityb[0])**2)+((citya[1]-cityb[1])**2))**0.5


#noofcities=4
dist={}
#dist[1,1]=0
#dist[1,2]=2
#dist[1,3]=1
#dist[1,4]=3
#dist[2,1]=2
#dist[2,2]=0
#dist[2,3]=4
#dist[2,4]=9
#dist[3,1]=1
#dist[3,2]=4
#dist[3,3]=0
#dist[3,4]=6
#dist[4,1]=3
#dist[4,2]=9
#dist[4,3]=6
#dist[4,4]=0
#ordering=[2,3,4]
for i in range(1,noofcities+1):
    for j in range(1,noofcities+1):
       dist[i,j]=distbwcities(cities[i],cities[j]) 


def get_subsets(fullset,m):
  import itertools
  subsets=[]
  X=list(itertools.combinations(fullset, m))
  for x in X:
      x=(1,)+x
      subsets.append(x)
  return subsets

def copyofswithoutj(s,j):
    p=()
    for element in s:
        if element==j:
            continue
        else:
            p+=(element,)
    return p
            
    
#a={}
#a[(1,),1]=0
#def TSP():
a={}
a[(1,),1]=0
for m in range(1,noofcities):#4
    #subset of size m+1
    if m>3:#%2==0 and m>3:
        b={}
        for x in a:
            if len(x[0])==m:#-1 or len(x[0])==m:
                b[x]=a[x]
        a=b
    print(m)
    S = get_subsets(ordering,m)
#    print(S)
    for s in S:
        a[s,1]=99999999

    for s in S:
#        print(s)
        possibilities=[]
        for j in s[1:]:
            possibilities=[]
            for k in s:
#                print("j",j)
#                print("k",k)
                flag=False
            #    if (m+1)>2 and k==1:
             #       flag=True
                if k!=j:# and flag==False:
                    p=copyofswithoutj(s,j)
#                    print(a[p,k]+dist[k,j])
                    possibilities.append(a[p,k]+dist[k,j])
#            print(possibilities)
            try:
             minpath=min(possibilities)
             a[s,j]=minpath
 #            print(minpath)
            except:
                continue
print(len(a),len(b)) 
                
#TSP()                 
realans=[]      
almostcompletepath=()
for x in range(1,noofcities+1):  
    almostcompletepath+=(x,)
for j in ordering:
    print(j,a[almostcompletepath,j])
    realans.append(a[almostcompletepath,j]+dist[j,1])
#            
print(min(realans))
end=time.time()
x2=float(end-start)
print(end-start)
####TSP()        
##        
#        
        