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



# def main():
#
#     file=open("PRIM.txt","r")
#     t=file.readline().split(" ")
#     n=int(t[0])
#     m=int(t[1])
#     edges=[]
#     for i in range(m):
#         t=file.readline().split(" ")
#         edges.append([int(t[0]),int(t[1]),int(t[2])])

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
        print(e)



# visited=[500]
# notvisited=list(range(1,500,1))
# cost=0
# def PRIM(edges):
#  #   print(visited)
#     global cost
#     flag=True
#     while flag!=False:
#      minimizethis=[]
#      flag=False
#      for edge in edges:
#         if edge[0] in visited and edge[1] in notvisited:
#         #    print(edge)
#             flag=True
#             minimizethis.append((edge[2],edge[0],edge[1]))
#         if edge[0] in notvisited and edge[1] in visited:
#         #    print(edge)
#             flag=True
#             minimizethis.append((edge[2],edge[1],edge[0]))
#      if flag==True :
#       minimizethis.sort()
#       edgechosen=minimizethis[0]
#       cost+=edgechosen[0]
#       visited.append(edgechosen[2])
#       notvisited.remove(edgechosen[2])
#     return(cost)
# print("Minimum Cost Spanning Tree Cost:")
# print(PRIM(edges))
#

if __name__=="__main__":
    main()
