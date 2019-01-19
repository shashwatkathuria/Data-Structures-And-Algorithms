# -*- coding: utf-8 -*-
"""
Created on Sat May 26 17:13:57 2018

@author: Shashwat Kathuria
"""

# KARGER'S RANDOMIZED MINCUT ALGORITHM (FOR UNDIRECTED GRAPH)

import random

# Declaring lists to store edges
edgesList, edgeListCopy1, newModifiedEdgeList = [], [], []

def main():
        global edgeListCopy1, newModifiedEdgeList, edgesList

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

                # Declaring modified new edge list
                newModifiedEdgeList = []

                for edgeNo in range(len(edgeListCopy1)):

                        # Not adding the random edge to new edge list
                        if edgeListCopy1[edgeNo] == randomEdge:
                            continue

                        # Renaming adjacent edges with the name of merged vertex
                        elif removeVertex == edgeListCopy1[edgeNo][0]:
                            shiftVertexPosition = edgeListCopy1[edgeNo][1]
                            # newModifiedEdgeList.remove(edgeListCopy1[edgeNo])
                            modifiedMergedEdge = ( saveVertex, shiftVertexPosition )

                            # Checking for self loop
                            if modifiedMergedEdge[0] != modifiedMergedEdge[1]:
                                newModifiedEdgeList.append( modifiedMergedEdge )

                        # Renaming adjacent edges with the name of merged vertex
                        elif removeVertex == edgeListCopy1[edgeNo][1]:
                            shiftVertexPosition = edgeListCopy1[edgeNo][0]
                            # newModifiedEdgeList.remove(edgeListCopy1[edgeNo])
                            modifiedMergedEdge = ( saveVertex, shiftVertexPosition )

                            # Checking for self loop
                            if modifiedMergedEdge[0] != modifiedMergedEdge[1]:
                                newModifiedEdgeList.append( modifiedMergedEdge )

                        else:
                            # Checking for self loop
                            if edgeListCopy1[edgeNo][0] != edgeListCopy1[edgeNo][1]:
                                newModifiedEdgeList.append(edgeListCopy1[edgeNo])

                # We update the newModifiedEdgeList to be an empty list in the next
                # iteration, assuming no aliasing effect of that on edgeListCopy1, this works
                # more efficiently then if we copy the newModifiedEdgeList to edgeListCopy1
                edgeListCopy1 = newModifiedEdgeList#[:]

            # Adding MinCut of current iteration to possibilities list
            possibilities.append(len(newModifiedEdgeList))

            # Printing result found till now
            print("MinCut obtained till now : " + str(min(possibilities)) + "\t\tLast added MinCut :" + str(possibilities[ - 1 ]) + "\n\n ")

def getVertexMergingCriteria(edge):

    # Criteria to merge the 2 vertices of an edge into 1
    # The one with small numerical value represents the merged vertex
    if edge[0] > edge[1]:
        return edge[1], edge[0]
    else:
        return edge[0], edge[1]


if __name__ == "__main__":
     main()
