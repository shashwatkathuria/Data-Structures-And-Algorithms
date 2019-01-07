# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 14:26:41 2018

@author: Shashwat Kathuria
"""

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
        self.vertices = list( range(1, 500, 1) )
        self.noOfEdges = 0

    def addEdge(self, edge):
        self.edges.append(edge)
        self.noOfEdges += 1
# path=False
# def DFS(graph,vertex,vertex2):
#   global path
#   path=False
#  # print(graph)
#   for key in graph:
#  #     print(key)
#       graph[key][0]=False
#   def DFS1(graph,vertex,vertex2):
#      global path
#      (graph[vertex])[0]=True
#      flag=True
#      neighbours=(graph[vertex])[1:]
#      if neighbours == []:
# #         print("No such path")
#          path = False
#          return
#      for neighbour in neighbours:
#            if graph[neighbour][0]==False:
#                flag=False
#      if flag==True:
#            path =  False
# #           print("There is no such path")
#            return
#
#      for neighbour in neighbours:
#              if (graph[neighbour])[0]==False:
#                if neighbour==vertex2:
#   #                 print(neighbour)
#                    path=True
# #                   print("Yes,there is a path")
#                    return
#                else:
#                    DFS1(graph,neighbour,vertex2)
#   DFS1(graph,vertex,vertex2)
#   return path
#
#
# l=[]
# for i in range(0,501,1):
#     l.append([i])
# def Merge(listi,listj):
#     ltemp=listi[:]+listj[:]
#     l.remove(listj)
#     l.remove(listi)
#     l.append(ltemp)

def main():
    file = open("CLUSTERING_1.txt","r")
    noOfVertices = int(file.readline())
    noOfEdges = ( noOfVertices * (noOfVertices - 1) ) / 2

    g = UndirectedGraph(noOfVertices)

    for i in range(1, noOfEdges + 1, 1):
        tempEdge = file.readline().split(" ")
        edge = Edge( u = int(tempEdge[0]), v = int(tempEdge[1]), distance = int(tempEdge[2]) )
        g.addEdge(edge)
        print(str(edge) + "\n" + str(i))

    g.edges.sort(key = lambda fn : fn.distance)


    # # edges=[[distance,vertex1,vertex2]]
    #  edges.sort()



#
# def findIndex(element):
#     for i in range(len(l)):
#      if element in l[i]:
#         break
#     return i
# graph={}
# for i in range(1,501,1):
#     graph[i]=[False]
# minimizethis=[]
# s1=0
# cost=0
# def Clustering(edges,noOfClusters):
#     global s1
#     global cost
#     for k in range(len(edges)):
#             print(k)
#             edge=edges[k]
#
#             vertex1=edge[1]
#             vertex2=edge[2]
# #            try:
#             if DFS(graph,vertex1,vertex2)==False:
#               graph[vertex1].append(vertex2)
#               graph[vertex2].append(vertex1)
#               cost+=edge[0]
#               s1+=1
#             else:
#                 minimizethis.append(edge[0])
#                 continue
# #            except:
#             i=findIndex(vertex1)
#             j=findIndex(vertex2)
#
#             if i==j:
#                 continue
#             else:
#                 Merge(l[i],l[j])
#             if len(l)==noOfClusters + 1:
#                 break
#     return k
# print(Clustering(edges,1))


if __name__ == "__main__":
    main()
