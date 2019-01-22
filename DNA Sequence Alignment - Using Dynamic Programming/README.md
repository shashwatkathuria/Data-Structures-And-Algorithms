# DNA SEQUENCE ALIGNMENT - USING DYNAMIC PROGRAMMING
------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------------

The following command must be executed to run the program:

      python sequencealignment.py


------------------------------------------
ALGORITHM
------------------------------------------

In DNA Sequence Alignment Algorithm, two DNA sequences are
analyzed and their best possible alignment to reduce their
cost (probability of transition of one to other) is computed.
In the base case, every string is matched with an empty string
character ' ' so the top column and leftmost row contain
number of characters of respective string computed * gap penalty.
In the dynamic approach cases, the ith and jth character of the
respective sequences can be compared in 4 ways: ith with jth,
ith with gap, jth with gap or gap with gap. The gap with gap case
is redundant as we can as well remove the corresponding gaps so we
ignore it and compute the rest to get the answer. Then we backtrack
by analyzing the options which were chosen earlier and then output
the result. The run time complexity of this algorithm is O(m * n)
where m is the length of the first sequence and n is the length of
the second sequence. The i and j above correspond to the respective
iteration values of the rows and columns of the dynamic programming
matrix respectively.

------------------------------------------   
