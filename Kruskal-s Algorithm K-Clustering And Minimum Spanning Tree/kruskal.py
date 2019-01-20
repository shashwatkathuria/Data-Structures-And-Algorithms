# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:26:41 2018

@author: Shashwat Kathuria
"""

# Kruskal's Algorithm - K - Clustering and Minimum Spanning Tree - Greedy Algorithm

def main():

    # Reading from the input file and storing the edges in a graph
    file = open("CLUSTERING_1.txt","r")
    noOfVertices = int(file.readline())
    noOfEdges = ( noOfVertices * (noOfVertices - 1) ) / 2

    # Declaring graph to store the input graph
    originalGraph = UndirectedGraph(noOfVertices)

    for i in range(1, noOfEdges + 1, 1):
        tempEdge = file.readline().split(" ")
        edge = UndirectedEdge( u = int(tempEdge[0]), v = int(tempEdge[1]), distance = int(tempEdge[2]) )
        originalGraph.addEdge(edge)
        print("ADDED EDGE : " + str(edge) )

    # Declaring a new cluster graph to store the result of the kruskal's algorithm
    clusterGraph = ClusterGraph( 500 )

    # Prompting user for the number of clusters required (1 for minimum spanning tree)
    n = input("Enter the number of clusters you want (1 for MST) : ")

    # Calling kruskal's algorithm and printing the result of the algorithm
    print("The no of edges in the cluster are : " + str(kruskal(edges = originalGraph.edges, noOfClusters = n,graph = clusterGraph)))



def kruskal(edges, noOfClusters, graph):
    """Kruskal's Algorithm to find the best (minimum) possible sized clusters. Inputs are the edges, the cluster graph
       to store the inputs in, and the number of clusters required."""

    # Sorting the edges of the graph by their distance as it is a requirement of the greedy approach
    edges.sort(key = lambda fn : fn.distance)

    # Variable to store the cost of the cluster graph
    cost = 0

    # For loop to go through the edges of the graph in ascending order of their distances
    for noOfEdgesSurpassed in range(len(edges)):
            edge = edges[noOfEdgesSurpassed]

            vertex1 = edge.u
            vertex2 = edge.v

            # Adding edge to cluster graph if and only if there does not
            # already exist a path between the two vertices
            if DFS(graph, vertex1, vertex2) == False:
                graph.booleanVerticeTraversed[vertex1].append(vertex2)
                graph.booleanVerticeTraversed[vertex2].append(vertex1)
                graph.addEdge(edge)
                cost += edge.distance

                # Finding the corresponding cluster to which the vertices belong
                i = graph.findClusterIndex(vertex1)
                j = graph.findClusterIndex(vertex2)

                # Not adding them if they belong to the same cluster
                if i == j:
                    continue
                # Else merging their clusters
                else:
                    graph.mergeClusters(i,j)

                # Breaking from the for loop if the clusters required are formed
                if len(graph.clusters) == noOfClusters + 1:
                    print("\n\nFOLLOWING ARE THE CLUSTERS :- \n \n")
                    print(graph.clusters[1:])
                    print("\n\nThe cost of the cluster formation is : " + str(cost))
                    break

            # Else ignoring that edge and going on to next one as that will create a loop otherwise
            else:
                continue

    return noOfEdgesSurpassed


def DFS(graph, vertex, vertex2):
    path = False
    for key in graph.booleanVerticeTraversed:
        graph.booleanVerticeTraversed[key][0] = False

    def DFSHelper(graph, vertex, vertex2):
        global path
        graph.booleanVerticeTraversed[vertex][0] = True
        neighbours = graph.booleanVerticeTraversed[vertex][1:]

        if neighbours == []:
            path = False
            return


        flag = True
        for neighbour in neighbours:
            if graph.booleanVerticeTraversed[neighbour][0] == False:
                flag = False

        if flag == True:
            path = False
            return

        for neighbour in neighbours:
            if graph.booleanVerticeTraversed[neighbour][0] == False:
                if neighbour == vertex2:
                    path = True
                    return
                else:
                    DFSHelper(graph,neighbour,vertex2)

    DFSHelper(graph,vertex,vertex2)
    return path


class UndirectedEdge:

    def __init__(self, u, v, distance):
        """Funtion to initialize an edge."""
        self.u = u
        self.v = v
        self.distance = distance

    def __str__(self):
        """Funtion to print the edge in the required way."""
        return "Between {} and {}  Distance = {}".format(self.u, self.v, self.distance)

class UndirectedGraph:

    def __init__(self, noOfVertices):
        """Function to initialize the graph."""
        self.edges = []
        self.noOfVertices = noOfVertices
        self.vertices = list( range(1, noOfVertices + 1, 1) )
        self.noOfEdges = 0

    def addEdge(self, edge):
        self.edges.append(edge)
        self.noOfEdges += 1

class ClusterGraph:

    def __init__(self, noOfVertices):
        self.edges = []
        self.noOfVertices = noOfVertices
        self.clusters = []
        self.booleanVerticeTraversed = {}

        for i in range(1, self.noOfVertices + 1, 1):
            self.booleanVerticeTraversed[i] = [ False ]

        for i in range(0, noOfVertices + 1, 1):
            self.clusters.append([i])

    def addEdge(self, edge):
        self.edges.append(edge)

    def mergeClusters(self, i, j):
        listi = self.clusters[i]
        listj = self.clusters[j]
        ltemp = listi[:] + listj[:]
        self.clusters.remove(listi)
        self.clusters.remove(listj)
        self.clusters.append(ltemp)

    def findClusterIndex(self, element):
        for i in range( len(self.clusters) ):
            if element in self.clusters[i]:
                break
        return i


if __name__ == "__main__":
    main()
