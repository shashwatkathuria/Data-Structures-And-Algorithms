# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 07:31:55 2018

@author: Shashwat Kathuria
"""

# BELLMAN FORD ALL PAIRS SHORTEST PATH ALGORITHM

# ALL PAIRS SHORTEST PATHS

# Assignment answers
# g3 = -19
# g2, g1 = negative cycle

def main():

    # Reading the input file and saving corresponding graph and
    # edges info inside graph object
    file = open("g1.txt", "r")
    graphInfo = file.readline().split(" ")
    noOfVertices, noOfEdges1 = int(graphInfo[0]), int(graphInfo[1])
    directedGraph = DirectedGraph(noOfVertices = noOfVertices, noOfEdges = noOfEdges1)

    # For loop for g1.txt, g2.txt and g3.txt
    for i in range(noOfEdges1):
        s = file.readline().split(" ")
        edge = DirectedEdge( startVertex = int(s[0]), endVertex = int(s[1]), edgeWeight = int(s[2]) )
        print(edge)
        directedGraph.addEdge(edge)
        directedGraph.graph[edge.startVertex].append(edge.endVertex)

    ## For loop for dijkstraDataCopy.txt

    ## Only 1 for loop is to be used at a time, other is to be commented

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

    # Computing the indegree  neighbours for each vertex in graph
    directedGraph.computeInDegreeNeighbours()

    # Calling bellman ford algorithm on graph
    bellmanFord(directedGraph)


def bellmanFord(directedGraph):
    """Bellman Ford Algorithm function to compute all shortest paths.Inpuut is the directed graph."""

    n = directedGraph.noOfVertices # -1   <- if sure that no negative cycle is present
    # Boolean for keeping track for any negative cycle's presence
    negativeCycle = False

    # Looping for each source
    for source in range(1, directedGraph.noOfVertices + 1):

        # Initializing shortest paths of graphs with standard values
        for destination in range(1, directedGraph.noOfVertices + 1):

            for noOfEdgesTraversed in range(0, n + 1):

                if source == destination:
                    directedGraph.shortestPaths[source, destination, noOfEdgesTraversed] = 0
                else:
                    directedGraph.shortestPaths[source, destination, noOfEdgesTraversed] = 9999999

        # Looping for maximum number of edges allowed in the current path concerned
        for noOfEdgesTraversed in range(1, n + 1):

            print("COMPUTING SHORTEST PATHS FROM SOURCE VERTEX : " + str(source) + "  EDGES TRAVERSED COUNTER : " + str(noOfEdgesTraversed) )

            # Looping for each possible destination
            for vertex in range(1, directedGraph.noOfVertices + 1):

                # Storing previous value
                path1 = directedGraph.shortestPaths[source, vertex,noOfEdgesTraversed - 1]
                # List to store new candidates possible
                path2Candidates = []

                for neighbour in directedGraph.inDegreeNeighbours[vertex]:

                    path2Candidates.append( directedGraph.shortestPaths[source, neighbour, noOfEdgesTraversed - 1] + directedGraph.edges[neighbour, vertex] )

                # if new candidate paths are present, shortest path is the minimum of
                # the number of edges - 1 path and mimum of path2 candidates
                if path2Candidates != []:
                    minimumPath2Candidate = min(path2Candidates)
                    directedGraph.shortestPaths[source, vertex, noOfEdgesTraversed] = min(path1, minimumPath2Candidate)

                # else shortest path is the number of edges - 1 graph
                else:
                    directedGraph.shortestPaths[source, vertex, noOfEdgesTraversed] = path1

        # if the value of shortest path for any vertex changes from n - 1 to n edges,
        # it means the directed graph concerned has a negative cycle
        if directedGraph.shortestPaths[source, vertex, n] != directedGraph.shortestPaths[source, vertex, n - 1]:
            print("\n\nThis graph has a Negative Cycle present. Therefore, shortest path has no meaning for this graph.\n\n")
            negativeCycle = True
            break

    # if no negative cycles, go ahead and print the shortest path for each vertex and destination
    if negativeCycle == False:

        print("\n\nTHE SHORTEST PATHS ARE : \n\n")

        # Printing shortest paths for each source and destination
        for i in range(1, directedGraph.noOfVertices + 1):
            for j in range(1, directedGraph.noOfVertices + 1):
                print("The shortest path from " + str(i) + " to " + str(j) + " has distance : " + str(directedGraph.shortestPaths[i, j, n - 1]) )

        print("\n")

class DirectedEdge:

    def __init__(self, startVertex, endVertex, edgeWeight):
        """Function to initialize edge.Inputs are the start vertex, end vertex and the edge weight."""
        self.startVertex = startVertex
        self.endVertex = endVertex
        self.edgeWeight = edgeWeight

    def __str__(self):
        """Function to print the edge."""
        return "Edge from " + str(self.startVertex) + " to " + str(self.endVertex) + " Weight " + str(self.edgeWeight)

class DirectedGraph:

    def __init__(self,noOfVertices, noOfEdges):
        """Function to initialize the graph. Inputs are the number of vertices and number of edges."""
        self.edges = {}
        self.noOfVertices = noOfVertices
        self.noOfEdges = noOfEdges
        self.graph = {}
        for vertex in range(1, self.noOfVertices + 1):
            self.graph[vertex] = [False]# self.graph[vertex]=[Visited or Not,neighbour1,neighour2,..]
        self.inDegreeNeighbours = {}
        self.shortestPaths = {}

    def addEdge(self,directedEdge):
        """Funtion to add a directed edge to the graph list of edges."""
        self.edges[directedEdge.startVertex, directedEdge.endVertex] = directedEdge.edgeWeight

    def computeInDegreeNeighbours(self):
        """Computes the indegree neighbours of all the vertices of the graph
        and stores it in the format [vertexVisitedOrNotVisited,indegreeneighbour1,indegreeneighbour2,...]"""
        for vertex in range(1, self.noOfVertices + 1):
                print("COMPUTING IN DEGREE NEIGHBOURS ON VERTEX NUMBER : " + str(vertex))
                self.inDegreeNeighbours[vertex] = []
                for key in self.graph:
                    if vertex in self.graph[key][1:]:
                        self.inDegreeNeighbours[vertex].append(key)

if __name__ == "__main__":
    main()
