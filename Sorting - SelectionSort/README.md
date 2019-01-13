# SELECTION SORT
------------------------------------
# INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------

The input array of a 100,000 entries is already provided in IntegerArray.txt.

To run the program, the following command is to be executed:

          python selectionsort.py


------------------------------------
# ALGORITHM
------------------------------------

In Selection Sort algorithm, in every linear pass of the array, the smallest element
from the right subarray which is unsorted is put to the end of the left subarray which
is sorted. This linear pass is done n times to sort the array. The invariant maintained
is that the part of array from the first element to the ith element is sorted whereas
the other part,i.e, from i+1 th element to the last element is unsorted.The best case
as well as the worst case performances of this algorithm are O(n^2).
 

------------------------------------  
