# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:28:19 2018

@author: Shashwat Kathuria
"""

# PRIM'S ALGORITHM (FOR UNDIRECTED GRAPHS) - GREEDY ALGORITHM

def main():

    # Reading from the input file and storing the edges in a graph
    file = open("PRIM.txt", "r")
    graphInfo = file.readline().split(" ")

    # Storing graph info
    noOfVertices = int(graphInfo[0])
    noOfEdges = int(graphInfo[1])

    # Declaring new graph
    g = UndirectedGraph(noOfVertices)

    # Adding edges to the graph
    for i in range(noOfEdges):
        tempEdge = file.readline().split(" ")
        e = UndirectedEdge(u = int(tempEdge[0]), v = int(tempEdge[1]), weight = int(tempEdge[2]))
        g.addEdge(e)
        print("EDGE ADDED :  " + str(e))

    # Calling the prim's algorithm on the graph, starting with vertex 1 (can be any)
    PrimsAlgorithm(graph = g, startVertex = 1)


def PrimsAlgorithm(graph, startVertex):
    """Funtion to compute the minimum spanning tree of the undirected graph.Inputs are the graph on which
       minimum spanning tree is to be computed and the start vertex of the minimum spanning tree(can be any)."""

    print("\n" + "COMPUTING MST .... " + "\n")
    cost = 0

    # Initializing conquered and unconquered territories
    visited = [ startVertex ]
    notvisited = list(range(1, 500, 1))
    edges = graph.edges
    isSpanAllVertices = False

    # List to store minimum spanning tree
    minimumSpanningTree = UndirectedGraph( noOfVertices = graph.noOfVertices )

    # Running algorithm until conquered territory spans all the vertices
    while isSpanAllVertices == False:
        # Flag to stop when all vertices are spanned
        isSpanAllVertices = True

        # List to store edges in current cut
        cutEdges = []

        # Finding edges passing from conquered to unconquered territory
        for edge in edges:

            # If such an edge found, adding it to possible edges list (cutEdges)
            if edge.u in visited and edge.v in notvisited:
                isSpanAllVertices = False
                # Saving edge in such a way that the unvisited vertex is signified by v attribute
                cutEdges.append( UndirectedEdge(u = edge.u, v = edge.v, weight = edge.weight) )

            elif edge.u in notvisited and edge.v in visited:
                isSpanAllVertices = False
                # Saving edge in such a way that the unvisited vertex is signified by v attribute
                cutEdges.append( UndirectedEdge(u = edge.v, v = edge.u, weight = edge.weight) )


        if isSpanAllVertices == False :
            edgechosen = min(cutEdges,key = lambda x: x.weight)
            minimumSpanningTree.addEdge( UndirectedEdge(u = edgechosen.u, v = edgechosen.v, weight = edgechosen.weight) )
            # Adding the unvisited vertex of the edge chosen to conquered territory and removing
            # the same from unconquered territory
            visited.append(edgechosen.v)
            notvisited.remove(edgechosen.v)

    # Printing the minimum spanning tree alongwith its cost in a sorted manner
    print("The minimum Spanning Tree is : \n")

    minimumSpanningTree.edges.sort(reverse = False, key = lambda x: x.u)

    for edge in minimumSpanningTree.edges:
        cost += edge.weight
        print(edge)

    print("\n" + "Minimum Cost Spanning Tree Cost:" + str(cost) + "\n")

    return

class UndirectedEdge:

    def __init__(self, u, v, weight):
        """Funtion to initialize undirected edge."""
        self.u = u
        self.v = v
        self.weight = weight

    def __str__(self):
        """Function to print the edge in the required way."""
        return "Between {} and {}  Weight = {}".format(self.u, self.v, self.weight)

class UndirectedGraph:

    def __init__(self, noOfVertices):
        """Function to initialize undirected graph"""
        self.edges  = []
        self.vertices = list( range(1, noOfVertices) )
        self.noOfEdges = 0
        self.noOfVertices = noOfVertices

    def addEdge(self, edge):
        """Funtion to add edge to the undirected graph. Input is the edge to be added."""
        self.edges.append(edge)
        self.noOfEdges += 1


if __name__ == "__main__":
    main()
