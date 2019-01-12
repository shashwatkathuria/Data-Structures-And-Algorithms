# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:22:57 2018

@author: Shashwat Kathuria
"""
# This program is for a directed graph
edges = []
startVertex = 1
noOfVertices = 200
visitedVertices = [ startVertex ]
notVisitedVertices = list(range(2, noOfVertices + 1, 1))
distances = [ 0 ] * 2
distances += [10000] * (noOfVertices - 1)

class DirectedEdge:

    def __init__(self, startVertex, endVertex, edgeWeight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.edgeWeight = edgeWeight

    def __str__(self):
        return "Edge from " + str(self.startVertex) + " to " + str(self.endVertex) + " Weight " + str(self.edgeWeight)

    def setDijkstraCriterion(self, dijkstraCriterion):
        self.dijkstraCriterion = dijkstraCriterion

def main():

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

    dijkstra(edges)

    print("\n\nTHE SHORTEST PATHS ARE : \n\n")

    for i in range(1, len(distances)):
        print("The shortest path from " + str(startVertex) + " to " + str(i) + " has distance : " + str(distances[i]) )

    print("\n")

def dijkstra(edges):
    flag = True
    while flag != False:
        flag = False
        minimizingCandidateEdges = []

        for directedEdge in edges:

            if (directedEdge.startVertex in visitedVertices) and (directedEdge.endVertex in notVisitedVertices):
                flag = True
                dijkstraCriterion = distances[ directedEdge.startVertex ] + directedEdge.edgeWeight
                directedEdge.setDijkstraCriterion(dijkstraCriterion)
                minimizingCandidateEdges.append( directedEdge )
            else:
                continue

        if flag == True:
            minimizingCandidateEdges.sort(reverse = False, key = lambda x: x.dijkstraCriterion)
            minimumDijkstraCriterionEdge = minimizingCandidateEdges[0]
            distances[ minimumDijkstraCriterionEdge.endVertex ] = minimumDijkstraCriterionEdge.dijkstraCriterion
            visitedVertices.append(minimumDijkstraCriterionEdge.endVertex)
            notVisitedVertices.remove(minimumDijkstraCriterionEdge.endVertex)
        else:
            return


if __name__ == "__main__":
    main()
