# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:22:57 2018

@author: Shashwat Kathuria
"""

# DIJKSTRA'S ALGORITHM

# This program is for a directed graph

edges = []
startVertex = 1
noOfVertices = 200

# Initiaizing conquered territory with start vertex, which is vertex number 1
visitedVertices = [ startVertex ]

# Initiaizing all the other vertices in the unconquered territory
notVisitedVertices = list(range(2, noOfVertices + 1, 1))

# List to store shortest paths
distances = [ 0 ] * 2
distances += [10000] * (noOfVertices - 1)

class DirectedEdge:

    def __init__(self, startVertex, endVertex, edgeWeight):
        """Function to define a directed edge.Inputs are start vertex, end vertex and edge weight."""

        self.startVertex = startVertex
        self.endVertex = endVertex
        self.edgeWeight = edgeWeight

    def __str__(self):
        """Function to print edge."""
        return "Edge from " + str(self.startVertex) + " to " + str(self.endVertex) + " Weight " + str(self.edgeWeight)

    def setDijkstraCriterion(self, dijkstraCriterion):
        """Function to store/update current dijkstra criterion for edge."""
        self.dijkstraCriterion = dijkstraCriterion

def main():

    # Reading data from file and storing the edges in a list of edges
    file = open("dijkstraData.txt", 'r')

    for i in range(noOfVertices):

        vertexAndEdgesInfo = file.readline().split('\t')
        vertex = int( vertexAndEdgesInfo[0] )
        edgesInfo = vertexAndEdgesInfo[1 : -1]

        for edge in edgesInfo:

            edgeInfo = edge.split(',')
            directedEdge = DirectedEdge(startVertex = vertex, endVertex = int( edgeInfo[0] ), edgeWeight = int( edgeInfo[1] ))
            print("ADDED EDGE : " + str(directedEdge) )
            edges.append( directedEdge )

    # Calling dijkstra's algorithm on the graph
    dijkstra(edges)

    # Printing the actual values of the shortest paths
    print("\n\nTHE SHORTEST PATHS ARE : \n\n")

    for i in range(1, len(distances)):
        print("The shortest path from " + str(startVertex) + " to " + str(i) + " has distance : " + str(distances[i]) )

    print("\n")


def dijkstra(edges):
    flag = True

    # Iterates until the conquered territory has all the vertices reachable
    while flag != False:
        flag = False
        # List to store possible edges for minimum dijkstra criterion for current iteration
        minimizingCandidateEdges = []

        # Searching for possible edges and adding if necessary
        for directedEdge in edges:

            # if startvertex is in conquered territory and end vertex is in unconquered territory
            # add the edge to possible list of minimum dijkstra criterion edges
            if (directedEdge.startVertex in visitedVertices) and (directedEdge.endVertex in notVisitedVertices):
                flag = True
                # Computing and storing dijkstra's criterion
                dijkstraCriterion = distances[ directedEdge.startVertex ] + directedEdge.edgeWeight
                directedEdge.setDijkstraCriterion(dijkstraCriterion)
                minimizingCandidateEdges.append( directedEdge )
            # else continue looking for other possibilities
            else:
                continue

        # if there exists unconquered vertices, choose the edge with
        # minimum dijkstra's criterion and add the corresponding vertices
        # to conquered and unconquered territories as required
        if flag == True:
            minimizingCandidateEdges.sort(reverse = False, key = lambda x: x.dijkstraCriterion)
            minimumDijkstraCriterionEdge = minimizingCandidateEdges[0]
            distances[ minimumDijkstraCriterionEdge.endVertex ] = minimumDijkstraCriterionEdge.dijkstraCriterion
            visitedVertices.append(minimumDijkstraCriterionEdge.endVertex)
            notVisitedVertices.remove(minimumDijkstraCriterionEdge.endVertex)

        # else return
        else:
            return


if __name__ == "__main__":
    main()
