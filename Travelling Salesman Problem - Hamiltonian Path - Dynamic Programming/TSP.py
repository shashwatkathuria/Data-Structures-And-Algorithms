# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 11:06:39 2018

@author: Shashwat Kathuria
"""

# TRAVELLING SALESMAN PROBLEM - HAMILTONIAN PATH - USING DYNAMIC PROGRAMMING

import itertools

def main():

    # Reading inputs (city coordinates) from the input file
    file = open("TSP.txt", "r")
    noOfCities = int(file.readline())

    # Storing inputs inside a dictionary
    cities = {}

    for i in range(noOfCities):
        tempCityInfo = file.readline().split()
        cityCoordinates = [ float(tempCityInfo[0]), float(tempCityInfo[1]) ]
        cities[ i + 1 ] = cityCoordinates[:]

    # Initializing the cities to be visited except the start vertex, i.e., city 1
    cityIndicesExcluding1 = list( range(2, noOfCities + 1) )

    # Storing distances between cities (as every city is connected to the other)
    citiesDistance = {}
    for i in range(1, noOfCities + 1):
        for j in range(1, noOfCities + 1):
            citiesDistance[i, j] = distanceBetweenTwoCities(cities[i], cities[j])

    # Calling TSP algorithm
    TSP(noOfCities, cityIndicesExcluding1, citiesDistance)


def distanceBetweenTwoCities(cityA, cityB):
    """Function to compute the distance between two cities."""

    return ( ( (cityA[0] - cityB[0]) ** 2 ) + ( (cityA[1] - cityB[1]) ** 2) ) ** 0.5


def getSubsets(cityIndicesExcluding1, subsetSizeWithout1):
    """Function to get specific size subsets appending city 1 (start vertex) to each subset."""

    # Getting subsets of specific size excluding start vertex, i.e.,city 1 and without the city 1
    subsets = []
    X = list( itertools.combinations(cityIndicesExcluding1, subsetSizeWithout1) )

    # Appending start vertex, i.e., city 1 to each subset
    for x in X:
        x = ( 1, ) + x
        subsets.append( x )

    return subsets

def tupleCopyWithoutElement(s, element):
    """Function to return the copy of a subset without a particular element (city)."""

    tupleCopy = ()

    for iteratedElement in s:
        # Excluding the element not wanted in tuple copy
        if iteratedElement == element:
            continue
        # Adding all other vertices
        else:
            tupleCopy += ( iteratedElement, )

    return tupleCopy


def TSP(noOfCities, cityIndicesExcluding1, citiesDistance):
    """Function to compute the Hamiltonian Path(TSP) using dynamic programming approach.
       Inputs are the number of cities, the list of cities to be visited (except start vertex)
       and the dictionary of distances between cities."""

    # Initializing the DP Matrix
    # Dictionary because the subset is also to be saved alongwith end vertex as index of dictionary
    dpMatrixDict = {}

    # Base case
    dpMatrixDict[ ( 1, ), 1 ] = 0

    # Iterating to solve bigger subproblems using dynamic programming
    for subsetSizeWithout1 in range(1, noOfCities):

        # Subset is of size subsetSizeWithout1 + 1
        print("COMPUTING. ON ITERATION NUMBER : " + str(subsetSizeWithout1) + " OUT OF " + str(noOfCities - 1) )

        # Reducing computation by ignoring off the smaller subproblems solutions no longer required
        if subsetSizeWithout1 > 3:
            smallerEfficientDpMatrixDict = {}
            for key in dpMatrixDict:
                if len(key[0]) == subsetSizeWithout1:
                    smallerEfficientDpMatrixDict[key] = dpMatrixDict[key]
            dpMatrixDict = smallerEfficientDpMatrixDict

        # Getting the subsets reuired
        sizeSpecificSubsets = getSubsets(cityIndicesExcluding1, subsetSizeWithout1)

        # Base cases
        for subset in sizeSpecificSubsets:
            dpMatrixDict[subset, 1] = 99999999


        for subset in sizeSpecificSubsets:

            # Computing through each possible end vertex
            for j in subset[1:]:

                # List to store the candidates for minimums
                possibilities = []

                # Computing through each possible last hop
                for k in subset:

                    # Storing possibilities alongwith the end vertex
                    if k != j:
                        tupleCopy = tupleCopyWithoutElement(subset, j)
                        possibilities.append( dpMatrixDict[tupleCopy, k] + citiesDistance[k, j] )

                # Getting the minimum path from the possible minimum candidates
                try:
                    minimumPath = min(possibilities)
                    dpMatrixDict[subset, j] = minimumPath
                except:
                    continue


    # List for storing all final possible path candidates containing all the vertices
    # and a last hop between the start and end vertex to make a cycle
    finalHamiltonianPathCandidates = []

    # Final Set(and/or Subset) including all the vertices
    almostCompletePath = tuple(range(1, noOfCities + 1))

    # Adding the last hop of the cycle of hamiltonian path between the end and start vertex
    for j in cityIndicesExcluding1:
        finalHamiltonianPathCandidates.append( dpMatrixDict[almostCompletePath, j] + citiesDistance[j, 1] )

    # Getting the final minimum solution
    hamiltonianPathSolution = min(finalHamiltonianPathCandidates)

    # Printing the solution
    print("The optimal(minimum) length Hamiltonian path distance is : " +  str( hamiltonianPathSolution ) )

    return

if __name__ == "__main__":
    main()
