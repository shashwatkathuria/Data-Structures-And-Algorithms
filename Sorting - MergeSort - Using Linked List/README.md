# MERGE SORT
------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------

The input array of a 100,000 entries is already provided in IntegerArray.txt.

To run the program, the following commands are to be executed:

          gcc mergesort.cpp
          ./a.out


------------------------------------
ALGORITHM
------------------------------------

In Merge Sort algorithm, the array/subarrays are rescursively merged.First the subarray
calls merge sort on its two halves, then merges itself. In this way, in the base case,
the neighbouring elements merge themselves, then double their merging size from 2 to 4
by taking more adjacent neighbours, then double their size to 8, and so on until the 
whole array is sorted. In the intermediate steps, the merged subarrays are sorted. The 
best and worse case performances of this algorithm are both O(nlogn).

Additionally, because of linked list, we need to traverse through the list to get the
address of the middle element for merging purpose which we would otherwise achieve in O(1)
time in an array. This takes O(n) time and does not affect the big-oh time complexity of
the algorithm.  


------------------------------------  
