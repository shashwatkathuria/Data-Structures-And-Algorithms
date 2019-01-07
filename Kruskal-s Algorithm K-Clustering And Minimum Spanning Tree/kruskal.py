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

class ClusterGraph:

    def __init__(self, noOfVertices):
        self.edges = []
        self.noOfVertices = noOfVertices
        self.clusters = []
        self.booleanVerticeTraversed = {}

        for i in range(1, self.noOfVertices + 1, 1):
            self.booleanVerticeTraversed[i] = [False]
        for i in range(0, noOfvertices + 1, 1):
            self.clusters.append([i])

    def addEdge(self, edge):
        self.edges.append(edge)

    def mergeClusters(self, listi, listj):
        ltemp=listi[:]+listj[:]
        self.clusters.remove(listj)
        self.clusters.remove(listi)
        self.clusters.append(ltemp)

    def findClusterIndex(self, element):
        for i in range( len(self.clusters) ):
            if element in self.clusters[i]:
                break
        return i

# def DFS(graph,vertex,vertex2):
#   for key in graph.booleanVerticeTraversed:
#       graph.booleanVerticeTraversed[key][0]=False
#   def DFS1(graph,vertex,vertex2):
#      (graph.booleanVerticeTraversed[vertex])[0]=True
#      flag=True
#      neighbours=(graph.booleanVerticeTraversed[vertex])[1:]
#      if neighbours == []:
#          return False
#      for neighbour in neighbours:
#            if graph[neighbour][0]==False:
#                flag=False
#      if flag==True:
#            return False
#
#      for neighbour in neighbours:
#              if (graph[neighbour])[0]==False:
#                if neighbour==vertex2:
#                    return True
#                else:
#                    DFS1(graph,neighbour,vertex2)
#
#   return DFS1(graph,vertex,vertex2)
#
#
# l=[]
# for i in range(0,501,1):
#     l.append([i])


def main():
    file = open("CLUSTERING_1.txt","r")
    noOfVertices = int(file.readline())
    noOfEdges = ( noOfVertices * (noOfVertices - 1) ) / 2

    originalGraph = UndirectedGraph(noOfVertices)

    for i in range(1, noOfEdges + 1, 1):
        tempEdge = file.readline().split(" ")
        edge = Edge( u = int(tempEdge[0]), v = int(tempEdge[1]), distance = int(tempEdge[2]) )
        originalGraph.addEdge(edge)
        print(str(edge) + "\n" + str(i))

    originalGraph.edges.sort(key = lambda fn : fn.distance)


    # # edges=[[distance,vertex1,vertex2]]
    #  edges.sort()



#

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
#             vertex1 = edge.u
#             vertex2 = edge.v
#             if DFS(graph,vertex1,vertex2)==False:
#               graph.booleanVerticeTraversed[vertex1].append(vertex2)
#               graph.booleanVerticeTraversed[vertex2].append(vertex1)
#               cost += edge.distance
#               s1 += 1
#             else:
#                 minimizethis.append(edge.distance)
#                 continue
#             i = graph.findClusterIndex(vertex1)
#             j = graph.findClusterIndex(vertex2)
#
#             if i == j:
#                 continue
#             else:
#                 graph.mergeClusters(l[i],l[j])
#             if len(graph.clusters) == noOfClusters + 1:
#                 break
#     return k
print(Clustering(edges = originalgraph.edges, noOfClusters = 1))


if __name__ == "__main__":
    main()
