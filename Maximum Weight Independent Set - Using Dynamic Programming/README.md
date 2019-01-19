# MAXIMUM WEIGHT INDEPENDENT SET ALGORITHM (FOR PATH GRAPHS) - USING DYNAMIC PROGRAMMING
----------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
----------------------------------------

To following line must be executed to run the program:

        python MWIS.py

----------------------------------------
ALGORITHM
----------------------------------------

In MWIS Algorithm for path graphs, a set of nodes in a path
graph is to be chosen in such a way that no two nodes are
adjacent to each other and the sum of the weights of the nodes
of the set if maximum. That is done by starting from the starting node
of the path, analyzing two options - one that involves keeping the
ith node in the MWIS and one that involves not keeping the ith node
in the MWIS. Then, the maximum of the two answers is stored and then
going on to the next node and so on. In backtracking, the same options
are analyzed and if an option involves keeping the ith node, it is saved
in the MWIS. The run time complexity of this algorithm is O(n) where n
is the number of nodes in the path graph.

----------------------------------------
