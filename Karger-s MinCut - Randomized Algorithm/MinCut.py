# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:13:57 2018

@author: Shashwat Kathuria
"""
import random

edgeListCopy1,edgeListCopy2,edgesList = [], [], []

def main():
        global edgeListCopy1, edgeListCopy2, edgesList
        noOfVertices = 200
        edgesList = []
        file = open("kargerMinCut.txt", "r")

        for i in range(noOfVertices):
          t = file.readline()[ : - 2 ].split( '\t' )[ : - 1 ]
          Vertex = t[0]
          neighboursOfVertex = t[1:]
          for neighbour in neighboursOfVertex :
              edgesList.append( ( int(Vertex), int(neighbour) ) )

        for edge in edgesList:
            duplicateEdge = ( edge[1], edge[0] )
            if duplicateEdge in edgesList:
                edgesList.remove(duplicateEdge)

        possibilities = []

        nchoose2 = int( noOfVertices * ( noOfVertices - 1 ) / 2 )

        for k in range(nchoose2):

            print(str(k) + " LOOPS OUT OF " + str(nchoose2) + " COMPLETED (N choose 2).\n")
            edgeListCopy1 = edgesList[ : ]

            for i in range(noOfVertices - 2):
                randomEdge=random.choice(edgeListCopy1)

                saveVertex,removeVertex=getVertexMergingCriteria(randomEdge)

                edgeListCopy2=edgeListCopy1[:]

                edgeListCopy2.remove(randomEdge)
                edgeListCopy1.remove(randomEdge)

                for edge in edgeListCopy1:

                        if removeVertex == edge[0]:
                            shiftVertexPosition = edge[1]
                            edgeListCopy2.remove(edge)
                            modifiedMergedEdge = ( saveVertex, shiftVertexPosition )
                            edgeListCopy2.append( modifiedMergedEdge )

                        if removeVertex == edge[1]:
                            shiftVertexPosition = edge[0]
                            edgeListCopy2.remove(edge)
                            modifiedMergedEdge = ( saveVertex, shiftVertexPosition )
                            edgeListCopy2.append( modifiedMergedEdge )

                deleteSelfLoops()
                edgeListCopy1 = edgeListCopy2[:]
            possibilities.append(len(edgeListCopy2))
            print("MinCut obtained till now : " + str(min(possibilities)) + "\t\tLast added MinCut :" + str(possibilities[ - 1 ]) + "\n\n ")

def getVertexMergingCriteria(edge):
    if edge[0] > edge[1]:
        return edge[1], edge[0]
    else:
        return edge[0], edge[1]

def deleteSelfLoops():
    global edgeListCopy1, edgeListCopy2, edgesList
    temp = edgeListCopy2[:]
    for edge in temp:
        if edge[0] == edge[1]:
            edgeListCopy2.remove(edge)

if __name__ == "__main__":
     main()
