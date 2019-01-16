# QUICK SORT
------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------

The input array of a 10,000 entries is already provided in IntegerArray.txt.

To run the program, the following commands are to be executed:

          gcc quicksort.c
          ./a.out


------------------------------------
ALGORITHM
------------------------------------

In Quick Sort Algorithm, a pivot (an array element) is chosen in the array/subarray
and using it we sort the array. The pivot is compared to each element in such a way that
the elements smaller than it are to the left and the elements bigger than it are to
the left which corresponds to its correct position in the sorted array. The left and right
subarrays are then recursively called to the function excluding the pivot element. The pivot
is chosen in such a way that the split between the left and right subarrays are between
30/70 or 70/30 in percentage of the number of elements. The run time of this algorithm depends
on the choice of the pivots. The best case and worst case run time complexities of this algorithm
are respectively O(n^2) and O(nlogn) (average). In my version of the code, the pivot is chosen
as the median of the first, middle and end element of the subarray concerned.

------------------------------------  
