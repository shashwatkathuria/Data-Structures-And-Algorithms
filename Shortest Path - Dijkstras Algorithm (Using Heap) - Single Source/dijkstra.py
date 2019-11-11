# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:22:57 2018

@author: Shashwat Kathuria
"""

# DIJKSTRA'S ALGORITHM

# This program is for a directed graph
import time
edges = []
startVertex = 1
noOfVertices = 200

# Initiaizing conquered territory with start vertex, which is vertex number 1
visitedVertices = [ startVertex ]

# Initiaizing all the other vertices in the unconquered territory
notVisitedVertices = list(range(2, noOfVertices + 1, 1))

# List to store shortest paths
distances = [ 0 ] * 2
distances += [10000] * (noOfVertices - 1)

def main():
    t1 = time.time()
    # Reading data from file and storing the edges in a list of edges
    file = open("dijkstraData.txt", 'r')

    for i in range(noOfVertices):

        vertexAndEdgesInfo = file.readline().split('\t')
        vertex = int( vertexAndEdgesInfo[0] )
        edgesInfo = vertexAndEdgesInfo[1 : -1]

        for edge in edgesInfo:

            edgeInfo = edge.split(',')
            directedEdge = DirectedEdge(startVertex = vertex, endVertex = int( edgeInfo[0] ), edgeWeight = int( edgeInfo[1] ))
            print("ADDED EDGE : " + str(directedEdge) )
            edges.append( directedEdge )

    # Calling dijkstra's algorithm on the graph
    dijkstra(edges)

    # Printing the actual values of the shortest paths
    print("\n\nTHE SHORTEST PATHS ARE : \n\n")

    for i in range(1, len(distances)):
        print("The shortest path from " + str(startVertex) + " to " + str(i) + " has distance : " + str(distances[i]) )

    print("\n")
    t2 = time.time()
    print(t2-t1, "seconds time taken.")


def dijkstra(edges):
    """Function for dijkstra's algorithm."""

    # Initializing heap
    minimizingCandidateEdges = Heap(1 * len(edges), 4)

    # No vertices in candidate edges heap initially
    verticesInCurrentHeap = []

    # Initiaizing vertices in current heap with potential candidates from
    # source vertex initially
    for directedEdge in edges:
        # From conquered(start vertex) to unconquered territory
        # (all expect start vertex)
        if (directedEdge.startVertex == startVertex) and (directedEdge.endVertex != startVertex):
            verticesInCurrentHeap.append(directedEdge.endVertex)
            dijkstraCriterion = distances[ directedEdge.startVertex ] + directedEdge.edgeWeight
            directedEdge.setDijkstraCriterion(dijkstraCriterion)
            minimizingCandidateEdges.insertElement( directedEdge, minimizingCandidateEdges.getI() )
        else:
            continue

    # Variable to keep track of last removed vertex
    lastRemovedVertex = None

    # While all vertices are not conquered
    while len(visitedVertices) != noOfVertices:

            # Getting minimum candidate edge from heap
            minimumDijkstraCriterionEdge = minimizingCandidateEdges.extractMinimum()
            # Updating minimum distance in distances answer accordingly
            distances[ minimumDijkstraCriterionEdge.endVertex ] = minimumDijkstraCriterionEdge.dijkstraCriterion
            # Removing that edge
            minimizingCandidateEdges.removeMinimum()

            # Keeping track of indices to remove due to that edge
            indicesToRemove = []
            for i in range(minimizingCandidateEdges.i):
                edge = minimizingCandidateEdges.heap[i]
                # Continue if "NaN"
                if type(edge) == str:
                    continue
                # Remove if this condition holds true
                if edge.endVertex == minimumDijkstraCriterionEdge.endVertex:
                    indicesToRemove.append(i)

            # Removing all those edges from heap
            for i in indicesToRemove:
                minimizingCandidateEdges.removeMinimum(i)

            # Updating last removed vertex, conquered territory, unconquered
            # territory and vertices in current heap
            lastRemovedVertex = minimumDijkstraCriterionEdge.endVertex
            visitedVertices.append(lastRemovedVertex)
            notVisitedVertices.remove(lastRemovedVertex)
            verticesInCurrentHeap.remove(lastRemovedVertex)

            # Updating heap edges and adding new potential edges
            for directedEdge in edges:

                # From last removed vertex to unconquered territory
                if (directedEdge.startVertex == lastRemovedVertex) and (directedEdge.endVertex in notVisitedVertices):

                    # Required variables
                    flag = True
                    earlierDijkstraCriterion = None
                    newDijkstraCriterion = None

                    # If not in heap, then add edge
                    if (directedEdge.endVertex not in verticesInCurrentHeap):

                        verticesInCurrentHeap.append(directedEdge.endVertex)
                        dijkstraCriterion = distances[ directedEdge.startVertex ] + directedEdge.edgeWeight
                        directedEdge.setDijkstraCriterion(dijkstraCriterion)
                        minimizingCandidateEdges.insertElement( directedEdge, minimizingCandidateEdges.getI() )

                    # Else if present in heap, check for current dijkstra
                    # criterion and new dijkstra criterion, update if
                    # required
                    else:

                        # New possible dijkstra criterion
                        newDijkstraCriterion = distances[ directedEdge.startVertex ] + directedEdge.edgeWeight
                        removeIndex = None

                        # Getting earlier dijkstra edge and its older criterion
                        for i in range(minimizingCandidateEdges.i):
                            edge = minimizingCandidateEdges.heap[i]
                            if type(edge) == str:
                                continue
                            if edge.endVertex == directedEdge.endVertex:
                                earlierDijkstraCriterion = edge.dijkstraCriterion
                                removeIndex = i
                                break

                        # If found such an index
                        if removeIndex != None:

                            # Update if new dijkstra criterion is lesser than
                            # older one
                            if newDijkstraCriterion < earlierDijkstraCriterion:
                                minimizingCandidateEdges.removeMinimum(removeIndex)
                                directedEdge.setDijkstraCriterion(newDijkstraCriterion)
                                minimizingCandidateEdges.insertElement(directedEdge, minimizingCandidateEdges.getI())

                        # Else if not found such an index
                        else:
                            # If earlier dijkstra criterion is none, that is the
                            # edge doesn't exist in heap, then add the edge
                            if earlierDijkstraCriterion == None:
                                directedEdge.setDijkstraCriterion(newDijkstraCriterion)
                                minimizingCandidateEdges.insertElement(directedEdge, minimizingCandidateEdges.getI())

                            # If earlier dijkstra criterion is smaller and the
                            # edge doesn't exist in heap, then add the edge
                            elif newDijkstraCriterion > earlierDijkstraCriterion:
                                directedEdge.setDijkstraCriterion(earlierDijkstraCriterion)
                                minimizingCandidateEdges.insertElement(directedEdge, minimizingCandidateEdges.getI())


# Class for directed edge
class DirectedEdge:

    def __init__(self, startVertex, endVertex, edgeWeight):
        """Function to define a directed edge.Inputs are start vertex, end vertex and edge weight."""

        self.startVertex = startVertex
        self.endVertex = endVertex
        self.edgeWeight = edgeWeight

    def __str__(self):
        """Function to print edge."""
        try:
            return "Edge from " + str(self.startVertex) + " to " + str(self.endVertex) + " Weight " + str(self.edgeWeight) + " Dijkstra Criterion " + str(self.dijkstraCriterion)
        except:
            return "Edge from " + str(self.startVertex) + " to " + str(self.endVertex) + " Weight " + str(self.edgeWeight)
    def setDijkstraCriterion(self, dijkstraCriterion):
        """Function to store/update current dijkstra criterion for edge."""
        self.dijkstraCriterion = dijkstraCriterion


# Class for heap
class Heap:

    def __init__(self, noOfElements, limitOfRestructuring):
        """"Initializes heap instance.Inputs are no of elements in heap and limit of restructuring of heap."""

        self.heap = [ 'NaN' ] * noOfElements
        self.noOfElements = noOfElements
        self.i = 1
        self.noOfRemovedElements = 0
        self.limitOfRestructuring = limitOfRestructuring

    def __str__(self):
        """Defining str function to display/print heap."""

        string = "["
        for i in range(1, self.i , 1):
            try:
                string += str(self.heap[i]) + "\n"
            except:
                string += "Nan "
        return string + "]"

    def extractMinimum(self):
        """Function to return the minimum element of the heap"""

        return self.heap[1]

    def getI(self):
        """Function to return the position where the next element can be added."""

        return self.i

    def insertElement(self, element , i ):
        """Function to insert an element in the heap.Input is element to be added and i is the value returned from getI() function"""

        self.heap[i] = element
        # Parent of ith position
        parenti = i // 2

        # Inserting element into the heap
        try:
            # Bubbling up
            if parenti != 0 and self.heap[i].dijkstraCriterion < self.heap[parenti].dijkstraCriterion:
                self.heap[i], self.heap[parenti] = self.heap[parenti], self.heap[i]
                self.insertElement(element, parenti)
            # Incrementing self.i position
            else:
                self.i += 1
                return

        except:
            # Bubbling up
            self.heap[i] = 'NaN'
            self.insertElement(element, parenti)
            return

    def removeMinimum(self, i = 1):
        """Function to remove the minimum element in the heap."""

        # print("I", i, self.heap[i], self.noOfRemovedElements)

        # Base cases
        if self.heap[i] == 'NaN' :
            self.noOfRemovedElements += 1
            # Restructures heap to be a continuous list otherwise a lot of "Nan" noOfElements
            # due to removal of minimums a lot of times interfere with the logic of the program
            if self.noOfRemovedElements == self.limitOfRestructuring:
                self.restructureHeap()
                self.noOfRemovedElements  = 0
            return
        if 2 * i + 1 > self.noOfElements or 2 * i > self.noOfElements:
            self.heap[i] == "NaN"
            self.noOfRemovedElements += 1
            # Restructures heap to be a continuous list otherwise a lot of "Nan" noOfElements
            # due to removal of minimums a lot of times interfere with the logic of the program
            if self.noOfRemovedElements == self.limitOfRestructuring:
                self.restructureHeap()
                self.noOfRemovedElements  = 0
            return

        # Initializing children element positions
        child1 = 2 * i
        child2 = ( 2 * i ) + 1
        # print("child 1", child1, self.heap[child1])
        # print("child 2", child2, self.heap[child2])

        # Case when there are no children
        if self.heap[child1] == 'NaN' and self.heap[child2] == 'NaN':
            self.heap[i] = 'NaN'
            self.noOfRemovedElements += 1
            # Restructures heap to be a continuous list otherwise a lot of "Nan" noOfElements
            # due to removal of minimums a lot of times interfere with the logic of the program
            if self.noOfRemovedElements == self.limitOfRestructuring:
                self.restructureHeap()
                self.noOfRemovedElements  = 0
            return

        # Case when there is only one child
        elif self.heap[child2] == 'NaN':
            self.heap[i], self.heap[child1] = self.heap[child1], "NaN"
            self.noOfRemovedElements += 1
            # Restructures heap to be a continuous list otherwise a lot of "Nan" noOfElements
            # due to removal of minimums a lot of times interfere with the logic of the program
            if self.noOfRemovedElements == self.limitOfRestructuring:
                self.restructureHeap()
                self.noOfRemovedElements  = 0
            return

        # Case when there is only one child, same as above
        elif self.heap[child1] == 'NaN':
            self.heap[i], self.heap[child2] = self.heap[child2], "NaN"
            self.noOfRemovedElements += 1
            # Restructures heap to be a continuous list otherwise a lot of "Nan" noOfElements
            # due to removal of minimums a lot of times interfere with the logic of the program
            if self.noOfRemovedElements == self.limitOfRestructuring:
                self.restructureHeap()
                self.noOfRemovedElements  = 0
            return

        # Swapping parent with the smaller child
        # Bubbling down
        if self.heap[child1].dijkstraCriterion <= self.heap[child2].dijkstraCriterion:
            self.heap[i], self.heap[child1] = self.heap[child1], self.heap[i]
            self.removeMinimum( child1 )
        else:
            self.heap[i], self.heap[child2] = self.heap[child2], self.heap[i]
            self.removeMinimum( child2 )



    def restructureHeap(self):
        """"Function to restructure heap to store elements in a continuous fashion in the list."""

        self.i = 1
        # Storing the elements that already exist in a temporary list
        tempList = []
        for heapElement in self.heap:
            if heapElement != "NaN" :
                tempList.append( heapElement )

        # Initializing new heap
        self.heap = ["NaN"] * self.noOfElements

        # Storing all the elements in the temporary list in a continuous fashion in the new heap
        for element in tempList:
            self.insertElement(element, self.i)

# Calling main function
if __name__ == "__main__":
    main()
