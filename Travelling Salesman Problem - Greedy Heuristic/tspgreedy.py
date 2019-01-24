# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 19:25:25 2018

@author: Shashwat Kathuria
"""

# TRAVELLING SALESMAN PROBLEM - GREEDY HEURISTIC

# The answer is 1203406.5012708856

# Initializing values required

visitedCities = []
notVisitedCities = []
noOfCities = 0
cities = {}
distance = []

def main():

    global visitedCities, notVisitedCities, cities, noOfCities

    # Reading input city coordinates from file and storing them inside a dict
    file = open("TSP.txt", "r")
    noOfCities = int( file.readline() )

    for i in range(noOfCities):
        cityCoordinates = file.readline().split()
        cities[i + 1] = [float(cityCoordinates[1]), float(cityCoordinates[2])]

    # Initializing visited cities with start vertex
    visitedCities = [1]

    # Initializing not visited cities with all vertices except start vertex
    notVisitedCities = list( range(2, noOfCities + 1) )

    # Calling tsp greedy heuristic
    tspGreedyHeuristic()

def tspGreedyHeuristic():
    """Function to calculate minimum Hamiltonian path using greedy heuristic."""
    global visitedCities, notVisitedCities, cities, noOfCities

    # Variable to store the answer
    distanceCalc = 0

    # For loop to run until all the cities are visited
    for k in range(1, noOfCities):

        # Printing iteration number
        print( "COMPUTING...ON ITERATION NUMBER : " + str(k) + " OUT OF " + str(noOfCities - 1) )

        # Calling function to return the next smallest distance from the last
        # visited city and the city to which it has this distance and storing them
        distanceToBeAdded, nextCity = distanceFromCityi(lastVisitedVertex = visitedCities[-1],notVisitedCities = notVisitedCities)

        # Incrementing the answer by the above obtained distance
        distanceCalc += distanceToBeAdded

        # Appending the city to list of visited cities and removing it from list of not visited cities
        visitedCities.append(nextCity)
        notVisitedCities.remove(nextCity)

    # Printing start and end vertex of path
    print("The start vertex is : " + str(visitedCities[0]))
    print("The end vertex is : " + str(visitedCities[-1]))
    # Printing result by adding to the answer the last distance so as to complete
    # the Hamiltonian cycle
    print("The greedy heuristic answer is : " + str(distanceCalc + distanceBetweenCities(cities[1], cities[visitedCities[-1]])) )

def distanceBetweenCities(CityA, CityB):
    """Function to return the distance between two cities using their coordinates."""

    return ( ( (CityA[0] - CityB[0]) ** 2) + ( (CityA[1] - CityB[1]) ** 2) )**0.5

def distanceFromCityi(lastVisitedVertex, notVisitedCities):
    """Funtion to return the next smallest city distance and the corresponding city
       from the last visited vertex."""

    # List to store distances from the last vertex
    distance = []

    for j in notVisitedCities:
        # Appending all cities
        distance.append( [distanceBetweenCities(cities[lastVisitedVertex], cities[j]), j] )

    # Storing answer
    minimumDistanceAndCity = min(distance, key = lambda x: x[0])

    # Returning corresponding answer
    return minimumDistanceAndCity[0], minimumDistanceAndCity[1]

if __name__ == "__main__":
    main()
