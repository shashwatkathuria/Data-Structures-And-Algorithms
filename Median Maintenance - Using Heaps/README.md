# MEDIAN MAINTENANCE - USING HEAPS
--------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
--------------------------------------------

The following command must be executed to run the program:

          python MedianMaintenance.py

--------------------------------------------
ALGORITHM
--------------------------------------------

In the Median Maintenace Algorithm, two heaps keep track of
half of the number of elements processed till a certain
iteration, one containing more if the number of elements processed
is odd. The left heap is a max heap which has the largest element
of the left half as its root, and the right heap is a min heap which
has the smallest element of the right half as its root. In each
subsequent iteration, the element is compared to both the roots and
inserted into the appropriate half in such a way so that the number
of elements in both the heaps differ at most by one. If the element
in concern happens to be smaller than the left max heap root, it is
inserted into the left heap and the sizes are accordingly adjusted
so that the property of the heaps and number of elements are retained
and similarly vice versa for the right heap. In each iteration, the median
of the elements processed till now is added to the sum, considering
the right middle element as the median if the number of elements
processed is even and the middle element as the median if the number of
elements processed is odd.The run time complexity of the algorithm is
O(nlogn) where n is the number of input elements.

--------------------------------------------
