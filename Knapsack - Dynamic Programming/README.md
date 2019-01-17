# KNAPSACK ALGORITHM
-----------------------
INSTRUCTIONS TO RUN THE PROGRAM
-----------------------

The following commans are to be executed to run the program:

### BIG KNAPSACK

        python knapsackbig.py

### SMALL KNAPSACK

        python knapsacksmall.py

------------------------
ALGORITHM
------------------------

In the Knapsack Algorithm, we look at each item in the list of
available items. If the weight of that item is bigger than the
capacity, then we ignore that item. Otherwise, we compute the
value of knapsack once with storing that item and once without
storing that item and store the maximum of those values as the
answer of that iteration/call. The difference between the big
and small versions is that the big version uses memoization
and recursion to eliminate some already solved (repeated) cases
whereas small version does not. The running time complexities of
the small knapsack is O(n * W) where n is the number of items
and W is the capacity of knapsack, and that of the big knapsack
is the same but with better constants. The naive approach has a
run time complexity of O(2^n)

------------------------
