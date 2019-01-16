# HEAP SORT
------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------

The input array of a 100,000 entries is already provided in IntegerArray.txt.

To run the program, the following command is to be executed:

          python heapsort.py


------------------------------------
ALGORITHM
------------------------------------

In Heap Sort Algorithm, the input elements are first inserted into a min heap
one by one. Then, the minimum element of the heap is taken out in each iteration,
deleted from the heap and then stored in a list or array.This goes on for n number
of iterations where n is the number of elements in the heap initially.The best and worse
case performances are respectively O(nlogn) and O(n^2) depending on whether the heap is
balanced or not. In this python program, the heap is occasionally restructured so it takes
more time than actual cases. If the heap implementation of C++ code of 'Implementation - Heap'
directory would be used, it would be faster due to the allowance of the use of pointers in C++.  

------------------------------------  
