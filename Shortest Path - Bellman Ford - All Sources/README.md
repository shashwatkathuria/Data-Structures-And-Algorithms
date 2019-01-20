# BELLMAN FORD ALL PAIRS SHORTEST PATH ALGORITHM - USING DYNAMIC PROGRAMMING
-----------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
-----------------------------------------------------

The following command must be executed to run the program:

      python allpairsbellman.py

-----------------------------------------------------
ALGORITHM
-----------------------------------------------------

In Bellman Ford Algorithm, dynamic programming is used to
compute the shortest path value between all pairs of vertices.
For each source and destination, a for loop iterating over
the number of edges allowed in a path is run, starting from 1,
and in each iteration, two options are analyzed, one which gives
the shortest path between them in the number of edges in the current
iteration minus one and the other option is the minimum of a list
of shortest paths of the neighbouring in degree vertices of the vertex
of number of edges in the current iteration minus one in addition to  
a last hop of the edge connecting them. In such a way, we get the
shortest paths after n - 1 iterations, where n is the number of vertices.
To check if a negative cycle is present, we also run through one more
iteration with n edges and if the shortest path for any pair changes from
n - 1 edges to n edges, that implies that a negative cycle must be present
in the graph and thus shortest path would have no meaning for the graph.
Also, no more than n - 1 edges are required in a shortest path as n edges
will give a cycle and a positive cycle will add one more unnecessary vertex
and also increase the value of the shortest path. The run time complexity
of this algorithm is O(n * n * m) where n is the number of vertices and m
is the number of edges, also, because m <= n^2, the worst case boils down
to O(n^4).

-----------------------------------------------------
