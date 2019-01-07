# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 20:28:19 2018

@author: Shashwat Kathuria
"""

class Edge:
    def __init__(self, start, end, weight):
        self.start = start
        self.end = end
        self.weight = weight
    def __str__(self):
        return "Start = {}  End = {}  Weight = {}".format(self.start, self.end, self.weight)

class Graph:

    def __init__(self, noOfVertices):
        self.edges  = []
        self.vertices = list(range(1,noOfVertices))
        self.noOfEdges = 0

    def addEdge(self, edge):
        self.edges.append(edge)
        self.noOfEdges += 1



def main():

    file = open("PRIM.txt", "r")
    graphInfo = file.readline().split(" ")
    noOfVertices = int(graphInfo[0])
    noOfEdges = int(graphInfo[1])
    g = Graph(noOfVertices)

    for i in range(noOfEdges):
        tempEdge = file.readline().split(" ")
        e = Edge(start = int(tempEdge[0]), end = int(tempEdge[1]), weight = int(tempEdge[2]))
        g.addEdge(e)
        print("EDGE ADDED :  " + str(e))

    print("Minimum Cost Spanning Tree Cost:" + str(PRIM(graph = g, startVertex = 1)))




def PRIM(graph,startVertex):
    print(" COMPUTING MST .... ")
    cost = 0
    visited=[startVertex]
    notvisited=list(range(1,500,1))
    edges = graph.edges
    flag=True
    while flag!=False:
        minimizethis=[]
        flag=False
        for edge in edges:
            if edge.start in visited and edge.end in notvisited:
                flag=True
                minimizethis.append((edge.weight, edge.start, edge.end))
            if edge.start in notvisited and edge.end in visited:
                flag=True
                minimizethis.append((edge.weight, edge.end, edge.start))
        if flag==True :
            minimizethis.sort()
            edgechosen=minimizethis[0]
            cost+=edgechosen[0]
            visited.append(edgechosen[2])
            notvisited.remove(edgechosen[2])
    return cost



if __name__=="__main__":
    main()
