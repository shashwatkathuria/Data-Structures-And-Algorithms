# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 07:31:55 2018

@author: Shashwat Kathuria
"""

#ALL VERTICES SHORTEST PATHS

def main():

    file = open("g1.txt", "r")
    graphInfo = file.readline().split(" ")
    noOfVertices, noOfEdges1 = int(graphInfo[0]), int(graphInfo[1])
    directedGraph = DirectedGraph(noOfVertices = noOfVertices, noOfEdges = noOfEdges1)


    for i in range(noOfEdges1):
        s = file.readline().split(" ")
        edge = DirectedEdge( startVertex = int(s[0]), endVertex = int(s[1]), edgeWeight = int(s[2]) )
        print(edge)
        directedGraph.addEdge(edge)
        directedGraph.graph[edge.startVertex].append(edge.endVertex)

    # file = open("dijkstraDataCopy.txt", 'r')
    # noOfVertices = 200
    #
    # directedGraph = DirectedGraph(noOfVertices = 200, noOfEdges = 0)
    # for i in range(noOfVertices):
    #
    #     vertexAndEdgesInfo = file.readline().split('\t')
    #     vertex = int( vertexAndEdgesInfo[0] )
    #     edgesInfo = vertexAndEdgesInfo[1 : -1]
    #
    #     for edge in edgesInfo:
    #
    #         edgeInfo = edge.split(',')
    #         directedEdge = DirectedEdge(startVertex = vertex, endVertex = int( edgeInfo[0] ), edgeWeight = int( edgeInfo[1] ))
    #         print("ADDED EDGE : " + str(directedEdge) )
    #         directedGraph.addEdge( directedEdge )
    #         directedGraph.graph[directedEdge.startVertex].append(directedEdge.endVertex)


    directedGraph.computeInDegreeNeighbours()

    bellmanFord(directedGraph)


def bellmanFord(directedGraph):
    n = directedGraph.noOfVertices # -1   <- if sure that no negative cycle is present
    negativeCycle = False
    for source in range(1, directedGraph.noOfVertices + 1):

        for destination in range(1, directedGraph.noOfVertices + 1):

            for noOfEdgesTraversed in range(0, n + 1):

                if source == destination:
                    directedGraph.shortestPaths[source, destination, noOfEdgesTraversed] = 0
                else:
                    directedGraph.shortestPaths[source, destination, noOfEdgesTraversed] = 9999999

        for noOfEdgesTraversed in range(1, n + 1):

            print("COMPUTING SHORTEST PATHS FROM SOURCE VERTEX : " + str(source) + "  EDGES TRAVERSED COUNTER : " + str(noOfEdgesTraversed) )

            for vertex in range(1, directedGraph.noOfVertices + 1):
                path1 = directedGraph.shortestPaths[source, vertex,noOfEdgesTraversed - 1]
                path2Candidates = []

                for neighbour in directedGraph.inDegreeNeighbours[vertex]:

                    path2Candidates.append( directedGraph.shortestPaths[source, neighbour, noOfEdgesTraversed - 1] + directedGraph.edges[neighbour, vertex] )

                if path2Candidates != []:
                    minimumPath2Candidate = min(path2Candidates)
                    directedGraph.shortestPaths[source, vertex, noOfEdgesTraversed] = min(path1, minimumPath2Candidate)
                else:
                    directedGraph.shortestPaths[source, vertex, noOfEdgesTraversed] = path1

        if directedGraph.shortestPaths[source, vertex, n] != directedGraph.shortestPaths[source, vertex, n - 1]:
            print("\n\nThis graph has a Negative Cycle present. Therefore, shortest path has no meaning for this graph.\n\n")
            negativeCycle = True
            break

    if negativeCycle == False:

        print("\n\nTHE SHORTEST PATHS ARE : \n\n")

        for i in range(1, directedGraph.noOfVertices + 1):
            for j in range(1, directedGraph.noOfVertices + 1):
                print("The shortest path from " + str(i) + " to " + str(j) + " has distance : " + str(directedGraph.shortestPaths[i, j, n - 1]) )

        print("\n")

class DirectedEdge:

    def __init__(self, startVertex, endVertex, edgeWeight):
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.edgeWeight = edgeWeight

    def __str__(self):
        return "Edge from " + str(self.startVertex) + " to " + str(self.endVertex) + " Weight " + str(self.edgeWeight)

class DirectedGraph:

    def __init__(self,noOfVertices, noOfEdges):
        self.edges = {}
        self.noOfVertices = noOfVertices
        self.noOfEdges = noOfEdges
        self.graph = {}
        for vertex in range(1, self.noOfVertices + 1):
            self.graph[vertex] = [False]# self.graph[vertex]=[Visited or Not,neighbour1,neighour2,..]
        self.inDegreeNeighbours = {}
        self.shortestPaths = {}

    def addEdge(self,directedEdge):
        self.edges[directedEdge.startVertex, directedEdge.endVertex] = directedEdge.edgeWeight

    def computeInDegreeNeighbours(self):
        for vertex in range(1, self.noOfVertices + 1):
                print("COMPUTING IN DEGREE NEIGHBOURS ON VERTEX NUMBER : " + str(vertex))
                self.inDegreeNeighbours[vertex] = []
                for key in self.graph:
                    if vertex in self.graph[key][1:]:
                        self.inDegreeNeighbours[vertex].append(key)

if __name__ == "__main__":
    main()
