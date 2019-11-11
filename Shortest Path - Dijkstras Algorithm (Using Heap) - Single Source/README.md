# DIJKSTRA'S ALGORITHM - SINGLE SOURCE - USING HEAP
-------------------------------------------------------
INTRUCTIONS TO RUN THE PROGRAM
-------------------------------------------------------

The following command should be executed to run the program :

          python3 dijkstra.py

-------------------------------------------------------
ALGORITHM
-------------------------------------------------------

In Dijkstra's Algorithm, initially the start vertex is taken in the
conquered territory. Then, one by one edges which start from the conquered
territory and end in the unconquered territory with minimum dijkstra criterion
are selected and their corresponding end vertices are engulfed into the
conquered territory and that end vertex's shortest path is updated as the
minimum dijkstra criterion.The dijkstra criterion is the shortest path distance
to start vertex of edge plus the weight of the edge in between those territories.
It is must that the weights of the edges must be positive for the algorithm to be
correct. The run time of this algorithm is O(mlogn) if we make use of heaps to
select the minimum dijkstra criteria edge and O(mn) for the simple iterative
approach, where m is the number of edges and n is the number of vertices in the
graph. We have used heap in this algorithm, therefore the run time complexity
of this algorithm is O(mlogn).

-------------------------------------------------------
