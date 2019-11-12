# EDIT DISTANCE ALGORITHM - SPELL CHECKER - USING DYNAMIC PROGRAMMING
------------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------------

The following command must be executed to run the program:

      python3 editDistance.py


------------------------------------------
ALGORITHM
------------------------------------------

In Edit Distance Algorithm, one word is compared with each word
in the dictionary and their best possible alignment to reduce their
cost (probability of transition of one to other) is computed.
In the base case, every string is matched with an empty string
character ' ' so the top column and leftmost row contain
number of characters of respective string computed * gap penalty.
In the dynamic approach cases, the ith and jth character of the
respective sequences can be compared in 4 ways: ith with jth,
ith with gap, jth with gap or gap with gap. The gap with gap case
is redundant as we can as well remove the corresponding gaps so we
ignore it and compute the rest to get the answer.The run time
complexity of this algorithm is O(m * k * n) where m is the length of
the word query, k is the max length of a word in the dictionary and
n is the number of words in the dictionary. The i and j above correspond
to the respective iteration values of the rows and columns of the
dynamic programming matrix respectively. The same letter, mismatch and
gap penalties are 0, 1 and 2 respectively according to their probabilities
of occurence. The closest words are kept track of by seeing the current
score of the words being compared and accordingly added by seeing the
number of such words required and whether the word is closer to the
ones in the list already in each iteration.

------------------------------------------   
