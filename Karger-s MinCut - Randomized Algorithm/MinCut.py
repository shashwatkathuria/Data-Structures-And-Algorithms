# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:13:57 2018

@author: Shashwat Kathuria
"""

# KARGER'S RANDOMIZED MINCUT ALGORITHM (FOR UNDIRECTED GRAPH) 

import random

# Declaring lists to store edges
edgesList, edgeListCopy1, edgeListCopy2 = [], [], []

def main():
        global edgeListCopy1, edgeListCopy2, edgesList

        # Reading input file and storing edges is a list
        noOfVertices = 200
        edgesList = []
        file = open("kargerMinCut.txt", "r")

        for i in range(noOfVertices):
          t = file.readline()[ : - 2 ].split( '\t' )[ : - 1 ]
          Vertex = t[0]
          neighboursOfVertex = t[1:]
          for neighbour in neighboursOfVertex :
              edgesList.append( ( int(Vertex), int(neighbour) ) )

        # Keeping only one edge of a undirected edge, either (a, b) or (b, a)
        for edge in edgesList:
            duplicateEdge = ( edge[1], edge[0] )
            if duplicateEdge in edgesList:
                edgesList.remove(duplicateEdge)

        #  To store the mincut for each loop
        possibilities = []

        nchoose2 = int( noOfVertices * ( noOfVertices - 1 ) / 2 )

        # Running loop nC2 times to ensure that probability of finding
        # correct answer is near 1  ( 1/nC2 -> (Probability of finding a mincut in a iteration) * nC2)
        for k in range(nchoose2):

            print(str(k) + " LOOPS OUT OF " + str(nchoose2) + " COMPLETED (N choose 2).\n")
            edgeListCopy1 = edgesList[ : ]

            for i in range(noOfVertices - 2):

                # Choosing a random edge
                randomEdge = random.choice(edgeListCopy1)

                # Merging edge and its vertices
                saveVertex, removeVertex = getVertexMergingCriteria( randomEdge )

                edgeListCopy2 = edgeListCopy1[:]

                # Removing that edge from the edge copy lists
                edgeListCopy2.remove( randomEdge )
                edgeListCopy1.remove( randomEdge )

                # Renaming adjacent edges with the name of merged vertex
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

                # Deleting self loops
                deleteSelfLoops()
                edgeListCopy1 = edgeListCopy2[:]

            # Adding MinCut of current iteration to possibilities list
            possibilities.append(len(edgeListCopy2))

            # Printing result found till now
            print("MinCut obtained till now : " + str(min(possibilities)) + "\t\tLast added MinCut :" + str(possibilities[ - 1 ]) + "\n\n ")

def getVertexMergingCriteria(edge):
    # Criteria to merge the 2 vertices of an edge into 1
    # The one with small numerical value represents the merged vertex
    if edge[0] > edge[1]:
        return edge[1], edge[0]
    else:
        return edge[0], edge[1]

def deleteSelfLoops():
    global edgeListCopy1, edgeListCopy2, edgesList

    # temp defined to eliminate aliasing effect
    temp = edgeListCopy2[:]

    # Deleting self loops
    for edge in temp:
        if edge[0] == edge[1]:
            edgeListCopy2.remove(edge)

if __name__ == "__main__":
     main()
