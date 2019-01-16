2 - SUM ALGORITHM - USING HASH TABLE IMPLEMENTATION
----------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
----------------------------------------------------

To run the program, the following command is to be executed.

              python 2SUM.py

----------------------------------------------------
ALGORITHM
----------------------------------------------------

In the 2 - SUM Algorithm, we store each input element in a hash table and
then for searching whether any element satisfies the 2 - SUM property, we
search the value of the corresponding element ( sum - element ) in the hash
table. If the value exists inside the hash table, then the element satisfies
the 2 - SUM property for that value of the sum. In this program, we use a
Quick and Dirty Hash Function. The running time of this algorithm is
O(number of sums * no of input elements * average value of a separate chain (which
is constant and ignored in big oh complexity if the hash function is properly
implemented.) ) which is significantly faster than the naive
O(number of sums * no of input elements ^ 2) approach.

-----------------------------------------------------  
