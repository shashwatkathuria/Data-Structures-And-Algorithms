# TRAVELLING SALESMAN PROBLEM - GREEDY HEURISTIC
--------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
--------------------------------------------

The following command must be executed to run the program:


            python tspgreedy.py


--------------------------------------------
ALGORITHM
--------------------------------------------

In Travelling Salesman Greedy Heuristic, a Hamiltonian Path
covering all the vertices with minimum possible total distance
is calculated. In this algorithm, a start vertex is chosen, and
from that vertex the next possible vertex which is the smallest
possible distance away from it is selected and then from this chosen
vertex again a vertex with minimum path is chosen among the vertices
which have not been visited yet and so on until all the vertices are
visited. This yields the minimum greedy Hamiltonian Path. The run time
of this algorithm is O(n ^ 2) where n is the number of vertices or cities.

--------------------------------------------
