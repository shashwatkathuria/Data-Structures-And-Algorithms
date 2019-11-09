# DISJOINT SET - NUMBER OF DIGITS IN IMAGE RECOGNITION ALGORITHM
-------------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
-------------------------------------------------------

The following command must be executed to run the program:

          python3 disjointSet.py


-------------------------------------------------------
ALGORITHM
-------------------------------------------------------

In this algorithm, all image pixels are initialized to their own
disjoint set as the only element in that disjoint set. Then as we
iterate through all the image pixels, we keep checking for potential
neighbours to merge the disjoint sets of the current pixel and the
corresponding neighbour if condition to do that holds true. Finally,
after scanning through all image pixels, we terminate the algorithm and
get the output. The running time complexity of this algorithm is O(n ^ 2)
where n is the number of pixels in the image.

-------------------------------------------------------
