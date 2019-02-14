# TRAVELLING SALESMAN PROBLEM - HAMILTONIAN PATH - USING DYNAMIC PROGRAMMING
----------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
----------------------------------------------------

The following command must be executed to run the program:

          python TSP.py

----------------------------------------------------
ALGORITHM
----------------------------------------------------

In this algorithm, we compute the Travelling Salesman Path
using dynamic programming approach. The main approach is that
we solve smaller subproblems involving a subset of vertices
visited(exactly once each) and also remember the start and end
vertex of that path and using those smaller subproblems solve
the bigger subproblems finally getting the solution. We get the
optimal value of such a path by taking the minimum of all the
vertices which are not the start or end vertex over their
respective paths such that the path is the smaller subproblem
excluding the end vertex in the subset and to that appending
a last hop of the edge between the end vertex of that smaller
subproblem and the (actual) end vertex of the bigger subproblem.
The run time complexity of this algorithm is O(n^2 x 2^n) where
n is the number of vertices. This is a reduction from of the
naive brute force search which would instead take O(n!)=O(n^n)
time.
-----------------------------------------------------
