# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:06:39 2018

@author: Shashwat Kathuria
"""
import time
start = time.time()
file = open("tsp5.txt", "r")
noOfCities = int(file.readline())

cities = {}
for i in range(noOfCities):
    tempCityInfo = file.readline().split()
    cityCoordinates = [ float(tempCityInfo[0]), float(tempCityInfo[1]) ]
    cities[ i + 1 ] = cityCoordinates[:]

cityIndicesExcluding1 = list( range(2, noOfCities + 1) )

def distanceBetweenTwoCities(cityA, cityB):

    return ( ( (cityA[0] - cityB[0]) ** 2 ) + ( (cityA[1] - cityB[1]) ** 2) ) ** 0.5


#noOfCities=4
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
#cityIndicesExcluding1=[2,3,4]
for i in range(1, noOfCities + 1):
    for j in range(1, noOfCities + 1):
       dist[i, j] = distanceBetweenTwoCities(cities[i], cities[j])


def getSubsets(fullset, subsetSizeWithout1):
  import itertools
  subsets = []
  X = list( itertools.combinations(fullset, subsetSizeWithout1) )
  for x in X:
      x = ( 1, ) + x
      subsets.append( x )
  return subsets

def tupleCopyWithoutElement(s, element):

    tupleCopy = ()

    for iteratedElement in s:
        if iteratedElement == element:
            continue
        else:
            tupleCopy += ( element, )

    return tupleCopy


def TSP():
    a = {}
    a[ ( 1, ), 1 ] = 0
    for subsetSizeWithout1 in range(1, noOfCities):#4
        #subset of size m+1
        if subsetSizeWithout1 > 3:
            b = {}
            for x in a:
                if len(x[0]) == subsetSizeWithout1:#-1 or len(x[0])==m:
                    b[x] = a[x]
            a=b
        print(m)
        S = getSubsets(cityIndicesExcluding1, subsetSizeWithout1)
    #    print(S)
        for s in S:
            a[s, 1] = 99999999

        for s in S:
    #        print(s)
            possibilities=[]
            for j in s[1:]:
                possibilities=[]
                for k in s:
    #                print("j",j)
    #                print("k",k)
                    flag = False
                #    if (m+1)>2 and k==1:
                 #       flag=True
                    if k != j:# and flag==False:
                        p = tupleCopyWithoutElement(s,j)
    #                    print(a[p,k]+dist[k,j])
                        possibilities.append( a[p, k] + dist[k, j] )
    #            print(possibilities)
                try:
                    minpath = min(possibilities)
                    a[s, j] = minpath
     #            print(minpath)
                except:
                    continue

    realans = []
    almostcompletepath = ()
    for x in range(1, noOfCities + 1):
        almostcompletepath += ( x,)
    for j in cityIndicesExcluding1:
        print(j, a[almostcompletepath, j])
        realans.append( a[almostcompletepath, j] + dist[j, 1] )

    print( min(realans) )
end = time.time()
x2 = float(end - start)
print(end - start)
