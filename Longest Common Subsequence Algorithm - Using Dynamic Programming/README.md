SHASHWAT KATHURIA
B17CS050
CSE
ASSIGNMENT 7
--------------------------------------------------------
LONGEST COMMON SUBSEQUENCE PROBLEM-DYNAMIC PROGRAMMING
--------------------------------------------------------
1. "lcs.cpp" contains the program implemented.
2. "./a.out" contains the compiled code.
3. "ouput.txt" contains a sample output.
4. "readme.txt" is this file.
--------------------------------------------------------
TIME COMPLEXITY
--------------------------------------------------------
void longestCommonSubsequence(string s1,string s2)
    O(m*n)   where m = length of string1 , n = length of string2
    The function takes m*n complexity to fill the matrix entries and filling each entry takes
    constant number of steps.Printing also takes m*n complexity and backtraking takes at most
    linear steps as the longest common subsequence can be either of the two strings itself in the
    worst case.
--------------------------------------------------------
