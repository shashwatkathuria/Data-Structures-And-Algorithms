# HUFFMAN CODING ALGORITHM - GREEDY ALGORITHM
---------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
---------------------------------------------------

The following commands must be executed to run the program:

          g++ huffmancoding.cpp
          ./a.out

---------------------------------------------------
ALGORITHM
---------------------------------------------------

In Huffman Coding Algorithm, a set of codes for each alphabet
are given with alongwith their frequency of occurence in a
file. To compress this file, the codes are to be generated in
such a way that those occuring more frequently are to be
represented by less number of bits to save bits and those with
more number of bits are to be represented by more number of bits
because the codes (sequence of bits required to represent a alphabet)
have to be prefix free so that there is no ambiguity while reading
them. In each iteration of this greedy algorithm, two minimum
nodes (or already merged trees) are merged to have them under a
single tree as the siblings of the root of the new tree. This is
done till only one tree is left which is the optimal solution to
the huffman coding algorithm. The run time complexity of this
algorithm is O(n ^ 2) where n is the number of total frequencies
corresponding to each alphabet.

---------------------------------------------------  
