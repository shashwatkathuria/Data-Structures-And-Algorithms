AIM
-----------------------------------

The given program illustrates the Prim's Algorithm to compute the cost of the minimum spanning tree.

INTRODUCTION
--------------------

The minimum spanning tree (MST) problem, in addition to enjoying several applications,
is a uniquely great problem for the study of greedy algorithms. Unusually, several 
different greedy algorithms always compute an optimal solution. We begin here with the 
Dijkstra-esque Prim’s algorithm. The correctness proof requires understanding the subtly
beautiful structure of cuts in graphs, while its blazingly fast implementation relies on 
a deft application of the heap data structure.

INPUT FILE FORMAT
-----------------

The first line of the file contains the number of vertices and the number of edges in the 
input graph.The lines afterwards indicate the edges in the format:- 
                     {vertice 1} {vertice 2} {cost of edge}    
