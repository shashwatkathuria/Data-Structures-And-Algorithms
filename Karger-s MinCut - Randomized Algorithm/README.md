# KARGER'S MINCUT ALGORITHM (FOR UNDIRECTED GRAPHS) (RANDOMIZED ALGORITHM)
---------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
---------------------------------------------------

The following command must be executed to run the program:

      python MinCut.py

---------------------------------------------------
ALGORITHM
---------------------------------------------------

In Karger's MinCut Algorithm, for n choose 2 iterations,
a random edge is chosen n - 2 times (where n is the number
of vertices) so that in the end, only 2 vertices are left and
we can have the MinCut value the same as the original graph.
The 2 vertices of the random edge are merged into one and self
loops are deleted because they do not contribute to the MinCut
value. The probability of getting the MinCut right in one
iteration is 1/nC2, so to get the right MinCut, we run the
iterations nC2 times to get the probability close to 1.The run time
complexity of this algorithm is O(n^2).

---------------------------------------------------
