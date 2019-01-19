# PRIM'S ALGORITHM - GREEDY ALGORITHM
------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------

The following command must be executed to run the program:

            python prim.py

------------------------
ALGORITHM
------------------------

In Prim's Algorithm, a conquered territory (initialized with any start vertex)
is chosen in which we keep adding the vertices as we go through the algorithm.
To get the minimum spanning tree, we keep adding vertices to the conquered edges
with the greedy paradignm that we select the edge with the minimum weight of all
the edges starting the conquered territory and ending at the unconquered territory.
The end of the minimum weight edge thus chosen is then added to the conquered territory
and removed from the unconquered territory. In such a way, we go on till the
conquered territory spans all the vertices of the graph. The run time complexity of
this algorithm is O(m * n) and can be more efficient if heaps are used O(m * log n)
where n is the number of vertices and m is the number of edges.

------------------------
