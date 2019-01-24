# PAPADIMITRIOU'S ALGORITHM - 2-SAT PROBLEM - RANDOMIZED ALGORITHM
----------------------------------
INSTRUCTIONS TO RUN THE PROGRAM:
----------------------------------

The following command must be executed to run the program:

            python3 2SAT.py

----------------------------------
ALGORITHM
----------------------------------

In Papadimitriou's Algorithm, a number of clauses containing
literals in negated or unnegated form are given and the aim is
to find whether or not there exists a solution which can satisfy
all the clauses. Solution refers to value of the literals, where
one literal can be used in multiple places. In the algorithm,
on each iteration, clauses are checked until one which is not
satisfying is obtained. Then, a random literal of that clause is
chosen and the value of that literal is negated (not the clause).
So on, the clauses are checked until no clauses are there which
violate the property or the iterations run out, in which case the
2-SAT property is not achievable with the given clauses. The run time
complexity of this alorithm is O(n^3 * logn) where n is the number of
variables(literals). This algorithm is always correct on instances not
satisfiable and almost always correct (close to 1 probability) on
instances satisfiable.

----------------------------------
