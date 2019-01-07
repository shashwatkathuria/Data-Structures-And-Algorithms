# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:26:41 2018

@author: Shashwat Kathuria
"""
def main():
    file = open("CLUSTERING_1.txt","r")
    noOfVertices = int(file.readline())
    noOfEdges = ( noOfVertices * (noOfVertices - 1) ) / 2

    originalGraph = UndirectedGraph(noOfVertices)

    for i in range(1, noOfEdges + 1, 1):
        tempEdge = file.readline().split(" ")
        edge = Edge( u = int(tempEdge[0]), v = int(tempEdge[1]), distance = int(tempEdge[2]) )
        originalGraph.addEdge(edge)
        print("ADDED EDGE : " + str(edge) )

    originalGraph.edges.sort(key = lambda fn : fn.distance)
    clusterGraph = ClusterGraph( 500 )
    n = input("Enter the number of clusters you want (1 for MST) : ")

    print("The no of edges in the cluster are : " + str(Clustering(edges = originalGraph.edges, noOfClusters = n,graph = clusterGraph)))


class Edge:

    def __init__(self, u, v, distance):
        self.u = u
        self.v = v
        self.distance = distance

    def __str__(self):
        return "Between {} and {}  Distance = {}".format(self.u, self.v, self.distance)

class UndirectedGraph:

    def __init__(self, noOfVertices):
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



cost = 0
def Clustering(edges, noOfClusters, graph):
    global cost

    for noOfEdgesSurpassed in range(len(edges)):
            edge = edges[noOfEdgesSurpassed]

            vertex1 = edge.u
            vertex2 = edge.v

            if DFS(graph,vertex1,vertex2) == False:
                graph.booleanVerticeTraversed[vertex1].append(vertex2)
                graph.booleanVerticeTraversed[vertex2].append(vertex1)
                graph.addEdge(edge)
                cost += edge.distance

            else:
                continue

            i = graph.findClusterIndex(vertex1)
            j = graph.findClusterIndex(vertex2)
            if i == j:
                continue
            else:
                graph.mergeClusters(i,j)

            if len(graph.clusters) == noOfClusters + 1:
                print("\n\nFOLLOWING ARE THE CLUSTERS :- \n \n")
                print(graph.clusters[1:])
                print("\n\nThe cost of the cluster formation is : " + str(cost))
                break
    return noOfEdgesSurpassed



if __name__ == "__main__":
    main()
