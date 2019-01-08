# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:06:39 2018

@author: Shashwat Kathuria
"""

import itertools

def main():

    file = open("tsp_small.txt", "r")
    noOfCities = int(file.readline())

    cities = {}
    for i in range(noOfCities):
        tempCityInfo = file.readline().split()
        cityCoordinates = [ float(tempCityInfo[0]), float(tempCityInfo[1]) ]
        cities[ i + 1 ] = cityCoordinates[:]

    cityIndicesExcluding1 = list( range(2, noOfCities + 1) )

    citiesDistance = {}
    for i in range(1, noOfCities + 1):
        for j in range(1, noOfCities + 1):
            citiesDistance[i, j] = distanceBetweenTwoCities(cities[i], cities[j])


    TSP(noOfCities, cityIndicesExcluding1, citiesDistance)


def distanceBetweenTwoCities(cityA, cityB):

    return ( ( (cityA[0] - cityB[0]) ** 2 ) + ( (cityA[1] - cityB[1]) ** 2) ) ** 0.5


def getSubsets(wholeSet, subsetSizeWithout1):

  subsets = []
  X = list( itertools.combinations(wholeSet, subsetSizeWithout1) )
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
            tupleCopy += ( iteratedElement, )
    return tupleCopy


def TSP(noOfCities, cityIndicesExcluding1, citiesDistance):
    a = {}
    a[ ( 1, ), 1 ] = 0
    for subsetSizeWithout1 in range(1, noOfCities):
        # Subset is of size subsetSizeWithout1 + 1
        print("COMPUTING. Finishes at " + str(noOfCities - 1) + " :" + str(subsetSizeWithout1))
        if subsetSizeWithout1 > 3:
            b = {}
            for key in a:
                if len(key[0]) == subsetSizeWithout1:
                    b[key] = a[key]
            a = b
        sizeSpecificSubsets = getSubsets(cityIndicesExcluding1, subsetSizeWithout1)
        for subset in sizeSpecificSubsets:
            a[subset, 1] = 99999999

        for subset in sizeSpecificSubsets:
            possibilities = []
            for j in subset[1:]:
                possibilities = []
                for k in subset:
                    if k != j:
                        tupleCopy = tupleCopyWithoutElement(subset, j)
                        possibilities.append( a[tupleCopy, k] + citiesDistance[k, j] )
                try:
                    minpath = min(possibilities)
                    a[subset, j] = minpath
                except:
                    continue

    realAnswer = []
    almostCompletePath = ()
    for x in range(1, noOfCities + 1):
        almostCompletePath += ( x,)
    for j in cityIndicesExcluding1:
        # print(j, a[almostCompletePath, j])
        realAnswer.append( a[almostCompletePath, j] + citiesDistance[j, 1] )

    print("The optimal(minimum) length Hamiltonian path distance is : " +  str( min(realAnswer) ) )


if __name__ == "__main__":
    main()
