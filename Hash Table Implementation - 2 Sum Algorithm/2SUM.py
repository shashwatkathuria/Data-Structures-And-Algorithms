# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:30:13 2018

@author: shash
"""
l1=[[0]]*1328263
def hashfunction(number):
    if number<0:
        number=abs(number)
        number+=17
    str1=str(number)
    rem=number%17
    ans=""
    for i in range(len(str1)):
        if i%2==0:
            ans+=str1[i]
    ans+=str(rem)
    for i in range(len(str1)):
        if i%2==1:
            ans+=str1[i]
    return int(ans)%1328263
file=open("2SUM.txt","r")
l=[]
for i in range(1000000):
    z=int(file.readline())
    l.append([z,hashfunction(z)])
#assert False
file=open("2SUM.txt","r")

for i in range(1000000):
      print(i)
#      print(hashfunction(s))
#      print(s)
      ltemp=[]
   #   if s not in l1[hashfunction(s)]:
      ltemp=(l1[l[i][1]])[:]#.append(s)
      ltemp.append(l[i][0])
      l1[l[i][1]]=ltemp[:]
    #  print(l1[hashfunction(s)])

foundvalues=[]
for s in range(-9980,-9965,1):
      print(s)
      for pair in l:
          n=s-pair[0]
          if n in l1[hashfunction(n)]:
              foundvalues.append(s)
              break
        