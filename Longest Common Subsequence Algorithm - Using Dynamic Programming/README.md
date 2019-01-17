# LONGEST COMMON SUBSEQUENCE ALGORITHM - DYNAMIC PROGRAMMING
--------------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
--------------------------------------------------------

The following command must be executed to run the program :

              g++ lcs.cpp
              ./a.out


--------------------------------------------------------
ALGORITHM
--------------------------------------------------------

In the Longest Common Subsequence Algorithm, dynamic programming is
used to keep track of the maximum length of longest common subsequence
till that particular iteration, then, on backtrackinng, we are able to get
the longest common subsequence. Whenever we get on a iteration where the
two corresponding characters of the strings are equal, we add one to
the length plus the diagonally left top value before without those
characters. If we do not encounter same corresponding characters,
we keep the value of the maximum value obtained till then if one of
those corresponding characters weren't there. To get the subsequence,
we simply backtrack by analyzing which cases took us to the particular
position in the DP matrix. The algorithm runs in O(m * n) time where
m is the length of the first string and n is the length of second string.  

--------------------------------------------------------
