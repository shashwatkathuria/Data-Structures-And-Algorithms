# RADIX SORT - USING COUNTING SORT
------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------

The input array of a 100,000 entries is already provided in IntegerArray.txt.

To run the program, the following command is to be executed:

          python RadixSort.py


------------------------------------
ALGORITHM
------------------------------------

In Radix Sort Algorithm, a counting sort subroutine is used to
sort the array. In each iteration, the corresponding digit (imagine
appending zeros to the start if the number of digits are different for each
number) of each number is compared to sort the array using the counting
sort subroutine. The corresponding digit refers to the digits starting from
the last digit and going all the way to the starting digit, decrementing a
place left in each iteration. The counting sort subroutine keeps track of
the corresponding digits frequency and appropriately assigns position to
each element of the array in such a way that the array is sorted in those
corresponding digits. It incrementally sums up the counts and stores the output,
decrementing the corresponding counts one by one. The run time complexity of
this algorithm is O(k * n) where n is the number of elements in the array and
k is the maximum number of digits/bits (depending upon the base, e.g., 10 in
this program) required to represent the number.

------------------------------------
