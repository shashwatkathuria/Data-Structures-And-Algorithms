# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:39:35 2018

@author: shash
"""
import time
start=time.time()
heap=['Nan']*10000
i1=1
i2=1
def extractmin(heap):
    return heap[1]
  
def insert1(heap,element,i):
    global i1
    heap[i]=element
    parenti=i//2
    try:
     if parenti!=0 and heap[i]<heap[parenti]:
       heap[i],heap[parenti]=heap[parenti],heap[i]
       insert1(heap,element,parenti)
     else:
        i1+=1
        return
    except:
        heap[i]='Nan'
        insert1(heap,element,parenti)
        return
def insert2(heap,element,i):
    global i2
    heap[i]=element
    parenti=i//2
    try:
      if parenti!=0 and heap[i]<heap[parenti]:
        heap[i],heap[parenti]=heap[parenti],heap[i]
        insert2(heap,element,parenti)
      else:
        i2+=1
        return
    except:
        heap[i]='Nan'
        insert2(heap,element,parenti)
        return
def removemin(heap,i):
    if heap[i]=='Nan':
        return
    child1=2*i
    child2=(2*i)+1
    if heap[child1]=='Nan' and heap[child2]=='Nan':
        heap[i]='Nan'
        return
    elif heap[child2]=='Nan':
        if heap[child1]>heap[i]:
            heap[i],heap[child1]=heap[child1],heap[i]
            heap[child1]='Nan'
            return
    elif heap[child1]=='Nan':
        if heap[child2]>heap[i]:
            heap[i],heap[child2]=heap[child2],heap[i]
            heap[child2]='Nan'
            return
        

    if heap[child1]<=heap[child2]:
            heap[i],heap[child1]=heap[child1],heap[i]
            removemin(heap,child1)
    else:
            heap[i],heap[child2]=heap[child2],heap[i]
            removemin(heap,child2)

def check1(heap):
      global i1
      i1=1  
      decker=[]
      for h in heap:
          if h!="Nan":
              decker.append(h)
      heap=["Nan"]*100000
      for deck in decker:
          insert1(heap,deck,i1)
      return heap
          
def check2(heap):
      global i2
      i2=1
      decker=[]
      for h in heap:
          if h!="Nan":
              decker.append(h)        
      heap=["Nan"]*100000
      for deck in decker:
          insert2(heap,deck,i2)
      return heap



l=[]
file=open("Median.txt","r")
for i in range(10000):
    s=file.readline()
    s=int(s[:len(s)-1])
    l.append(s)


n1=i1
n2=i2
medians=[]
heaplow=['Nan']*100000
insert1(heaplow,(-l[1]),i)
heaphigh=['Nan']*100000
insert2(heaphigh,l[0],i2)
medians.append(6331)
medians.append(2793)
for i in range(2,10000):

#    print(heaplow[1:i1])
#    print(heaphigh[1:i2])
#    print("The medians{}".format(medians))
    if n1==n2:
         if l[i]<heaphigh[1]:
             insert1(heaplow,-l[i],i1)
             medians.append(-heaplow[1])
             n1+=1
         else:
             insert2(heaphigh,l[i],i2)
             medians.append(heaphigh[1])
             n2+=1
    elif n1==n2+1:
         if l[i]>(heaplow[1]*(-1)):
             insert2(heaphigh,l[i],i2)
             medians.append(-heaplow[1])
             n2+=1
             
         else:
             gadbadh=heaplow[1]*(-1)
             removemin(heaplow,1)
             insert2(heaphigh,gadbadh,i2)
             insert1(heaplow,-l[i],i1)
             medians.append(-heaplow[1])
             n2+=1
             
    elif n2==n1+1:
        if l[i]<heaphigh[1]:
            insert1(heaplow,-l[i],i1)
            medians.append(-heaplow[1])
            n1+=1
        else:
            gadbadh=heaphigh[1]
            removemin(heaphigh,1)
            insert1(heaplow,-gadbadh,i1)
            insert2(heaphigh,l[i],i2)
            medians.append(-heaplow[1])
            n1+=1
    if i%3000==0:
     heaplow=check1(heaplow) 
     heaphigh=check2(heaphigh)
#print()
#print()        
#print(heaplow[1:i1])
#print(heaphigh[1:i2])
end=time.time()
print()
print()
#print(medians)
print(sum(medians))
print(end-start)
            
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    