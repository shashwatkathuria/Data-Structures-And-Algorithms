#LONGEST COMMON SUBSTRING ALGORITHM - DYNAMIC PROGRAMMING
--------------------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
--------------------------------------------------------

The following command must be executed to run the program :

              python3 lcs.py


--------------------------------------------------------
ALGORITHM
--------------------------------------------------------

In the Longest Common Substring Algorithm, dynamic programming is
used to keep track of the maximum length of longest common substring
till that particular iteration, then, on backtracking, we are able to get
the longest common subsequence. Whenever we get on a iteration where the
two corresponding characters of the strings are equal, we add one to
the length plus the diagonally left top value before without those
characters. If we do not encounter same corresponding characters,
we set that value to be zero. As we go through the iterations, we store the
maximum value and the position of that maximum value in the dp matrix. To get
the substring, we simply cut the portion of any of the two strings by slicing
the strings previous some characters(where the number of such characters is the
maximum value of the longest common substring which we stored earlier) from that
particular saved position. The algorithm runs in O(m * n) time where
m is the length of the first string and n is the length of second string.  

--------------------------------------------------------
