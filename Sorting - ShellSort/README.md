# SHELL SORT
--------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
--------------------------------------

The following command must be executed to run the program:

            g++ shellsort.cpp
            ./a.out

--------------------------------------
ALGORITHM
--------------------------------------

In Shell Sort Algorithm, the main aim is to reduce the
bubbling or number of swaps required in insertion sort
in latter stages of the iteration. So, the main approach
is that the insertion sort starts taking place on elements
which are gap number of elements away from each other for
each such possible subarray in the original array. The gap
starts from half the number of elements in the array and
is reduced by a factor of two in every subarray insertion sort
carried out for all such possible subarrays and goes on until
the gap obtained is one, that is, the original insertion sort.
The array after this is then sorted. The run time complexity of
this algorithm is O(nlogn) where n is the number of elements in
the array.

--------------------------------------
