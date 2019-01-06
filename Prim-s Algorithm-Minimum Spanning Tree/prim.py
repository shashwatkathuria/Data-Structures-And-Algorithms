# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:28:19 2018

@author: Shashwat Kathuria
"""

class UndirectedEdge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight
    def __str__(self):
        return "Between {} and {}  Weight = {}".format(self.u, self.v, self.weight)

class UndirectedGraph:

    def __init__(self, noOfVertices):
        self.edges  = []
        self.vertices = list( range(1, noOfVertices) )
        self.noOfEdges = 0

    def addEdge(self, edge):
        self.edges.append(edge)
        self.noOfEdges += 1



def main():
    try:
        file = open("PRIM.txt", "r")
    except:
        print("Could Not Open The Input File. Error.")
        return
    graphInfo = file.readline().split(" ")
    noOfVertices = int(graphInfo[0])
    noOfEdges = int(graphInfo[1])
    g = UndirectedGraph(noOfVertices)

    for i in range(noOfEdges):
        tempEdge = file.readline().split(" ")
        e = UndirectedEdge(u = int(tempEdge[0]), v = int(tempEdge[1]), weight = int(tempEdge[2]))
        g.addEdge(e)
        print("EDGE ADDED :  " + str(e))

    print("\n" + "Minimum Cost Spanning Tree Cost:" + str( PrimsAlgorithm(graph = g, startVertex = 1) ) + "\n")




def PrimsAlgorithm(graph, startVertex):
    print("\n" + "COMPUTING MST .... " + "\n")
    cost = 0
    visited = [ startVertex ]
    notvisited = list(range(1, 500, 1))
    edges = graph.edges
    flag = True

    while flag != False:
        cutsEdges = []
        flag = False
        for edge in edges:
            if edge.u in visited and edge.v in notvisited:
                flag = True
                cutsEdges.append((edge.weight, edge.u, edge.v))

            if edge.u in notvisited and edge.v in visited:
                flag=True
                cutsEdges.append((edge.weight, edge.v, edge.u))

        if flag==True :
            cutsEdges.sort(key = lambda fn : fn[0])
            edgechosen = cutsEdges[0]
            cost += edgechosen[0]
            visited.append(edgechosen[2])
            notvisited.remove(edgechosen[2])

    return cost



if __name__ == "__main__":
    main()
