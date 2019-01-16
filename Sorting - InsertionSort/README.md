# INSERTION SORT
------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------

The input array of a 100,000 entries is already provided in IntegerArray.txt.

To run the program, the following command is to be executed:

          python insertionsort.py


------------------------------------
ALGORITHM
------------------------------------

In Insertion Sort Algorithm, the array elements are iterated through one by one
from the starting and the invariant maintained is that the left subarray uptil the
i th element is sorted and the right subarray is unsorted, where i is the i th
iteration. In each iteration the first element of the right unsorted subarray is
selected and is bubbled left to the place where it should be for the left subarray
to remain sorted. At the end of the n iterations, where n is the number of elements
in the array, the array is sorted. The best case and worst case performances of the
algorithm are respectively O(n) and O(n^2).

------------------------------------  
