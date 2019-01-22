# BINARY SEARCH ALGORITHM - USING RECURSION
-----------------------------
INSTRUCTIONS TO RUN THE PROGRAM
-----------------------------

The following command must be executed to run the program:

              g++ binarysearch.cpp
              ./a.out

-----------------------------
ALGORITHM
-----------------------------

In the Binary Search Algorithm, an element is to be
searched in an array of elements. The requirement of the
algorithm is that the array must be sorted. The element is
searched recursively in such a way that the middle element of
the array is analyzed and if it is equal to the element being
searched for, then the algorithm terminates, otherwise the
same algorithm is applied to the left part of the array if the
middle element is bigger than the element being searched for and
similarly on the right part of the array the same algorithm is
applied if the middle element is smaller than the element being
searched for. The run time complexity of this algorithm is O(logn)
according to Master's Theorem.

-----------------------------
