# KRUSKAL'S ALGORITHM - K-CLUSTERING AND MINIMUM SPANNING TREE - GREEDY ALGORITHM
-------------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
-------------------------------------------------------

The following command must be executed to run the program:

          python kruskal.py


-------------------------------------------------------
ALGORITHM
-------------------------------------------------------

In Kruskal's Algorithm, a greedy approach is used to cluster
the vertices of a graph with the minimum possible sum of distances
between individual edges, i.e., cost. The edges are iterated through
one by one in the ascending order of the distance between edges.
Initially, each vertex is in its own cluster, and then as the algorithm
proceeds, two clusters are merged if and only if there does not belong
a path between them(the vertices of the edge in consideration) and
they (the vetices) are not in the same cluster. In this way, clusters
keep on merging until we get the required number of clusters. The run time
of the algorithm is O(mlogm) which is equivalent to O(mlogn) [because m <= n^2]
if heaps are used, where m is the number of edges and n is the number of
vertices and O(m^2) for simple approach.

-------------------------------------------------------
