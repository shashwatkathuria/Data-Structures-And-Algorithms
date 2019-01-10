# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:49:45 2018

@author: shash
"""
import random
import math
satisfiable1=False
#random.seed(0)
#clauses=[[-1,2],[3,4],[-3,2],[-3,-4],[-3,4]]
#n=4
#options=[1,2,3,4]
file=open("2SAT1.txt")
n=int(file.readline())
clauses=[]
for i in range(n):
    t=file.readline().split()
    t=[int(t[0]),int(t[1])]
    clauses.append(t)

ans=[]
ans.append("NaN")
for x in range(1,n+1):
    x=random.random()
    if x>0.5:
        ans.append(True)
    else:
        ans.append(False)

def satisfiable(x):
       if x[0]<0:
           ans1=not(ans[abs(x[0])])
       else:
           ans1=ans[x[0]]
  #         print(ans1)
       if x[1]<0:
           ans2=not(ans[abs(x[1])])
  #         print(ans2)
       else:
           ans2=ans[x[1]]
          
       return ans1 or ans2
twonsquared=2*(n**2)
for k in range(int(math.log(n,2))):
   print(k)
   for j in range(twonsquared):       
#      print(j)
      flag=True
      s1=0        
      for x in clauses:
#        print(x,satisfiable(x))
        y=random.choices(x)[0]
        if satisfiable(x)==False:
          flag=False
          ans[abs(y)]=not(ans[abs(y)])
          break
        else:
            s1+=1
      print(s1)
      if flag==True:
          satisfiable1=True
          break
         
      
   if satisfiable1==True:
        print("Instance is satisfiable")
        print(ans)
        break
   
    
if satisfiable1==False:
    print("The instance is not satisfiable")
    
    
    
    