# FRACTIONAL KNAPSACK - GREEDY ALGORITHM
-----------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
-----------------------------------

The following command must be executed to run the program:

          python fractionalknapsack.py

-----------------------------------
ALGORITHM
-----------------------------------

In Fractional Knapsack Algorithm, a greedy approach is used
to get the optimum value of the knapsack. First, the items
are sorted in decreasing order of their ratios and then put
them one by one in the knapsack until there is less space than
sufficient to put a whole item left. Then we add the fractional
value of that item according to the size left in the knapsack.
The run time complexity of this algorithm is O(n * logn) where
n is the number of items available, which is mainly governed
by sorting procedure.

-----------------------------------
