# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:25:25 2018

@author: Shashwat Kathuria
"""

# The answer is 1203406.5012708856

visitedCities = []
notVisitedCities = []
noOfCities = 0
cities = {}
distance = []

def main():

    global visitedCities, notVisitedCities, cities, noOfCities

    file = open("TSP.txt", "r")
    noOfCities = int( file.readline() )

    for i in range(noOfCities):
        cityCoordinates = file.readline().split()
        cities[i + 1] = [float(cityCoordinates[1]), float(cityCoordinates[2])]

    visitedCities = [1]
    notVisitedCities = list( range(2, noOfCities + 1) )
    tspGreedyHeuristic()

def tspGreedyHeuristic():

    global visitedCities, notVisitedCities, cities, noOfCities

    distanceCalc = 0
    for k in range(1, noOfCities):
        print( "COMPUTING...ON ITERATION NUMBER : " + str(k) + " OUT OF " + str(noOfCities - 1) )
        distanceToBeAdded, nextCity = distanceFromCityi(lastVisitedVertex = visitedCities[-1],notVisitedCities = notVisitedCities)
        distanceCalc += distanceToBeAdded
        visitedCities.append(nextCity)
        notVisitedCities.remove(nextCity)

    print("The start vertex is : " + str(visitedCities[0]))
    print("The end vertex is : " + str(visitedCities[-1]))
    print(distanceCalc + distanceBetweenCities(cities[1], cities[visitedCities[-1]]) )

def distanceBetweenCities(CityA, CityB):

    return ( ( (CityA[0] - CityB[0]) ** 2) + ( (CityA[1] - CityB[1]) ** 2) )**0.5

def distanceFromCityi(lastVisitedVertex, notVisitedCities):

    distance = []

    for j in notVisitedCities:
           distance.append( [distanceBetweenCities(cities[lastVisitedVertex], cities[j]), j] )
    distance.sort(reverse = False, key = lambda x: x[0])

    return distance[0][0],distance[0][1]

if __name__ == "__main__":
    main()
