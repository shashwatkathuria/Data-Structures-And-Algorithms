# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:54:12 2019

@author: Shashwat Kathuria
"""

# LONGEST COMMON SUBTRING ALGORITHM - USING DYNAMIC PROGRAMMING

def main():

    # Taking input strings from the user
    string1 = input( "Enter the first string : " )
    string2 = input( "Enter the second string : " )

    # Calling longest common substring algorithm on the inputs
    longestCommonSubstring(string1, string2)


def longestCommonSubstring(string1, string2):
    """Function to compute the longest common substring of two strings. Inputs
       are the two strings to compute the same upon."""

    # Initializing DP Matrix and results information
    numberOfRowsDP = len(string1) + 1
    numberOfColumnsDP = len(string2) + 1
    initialLcsDpPosition = (0, 0)
    result = [0, initialLcsDpPosition]

    # Initializing DP Matrix with all zeros
    dpMatrix = []
    for i in range(numberOfRowsDP):
        listInitialize = []
        for j in range(numberOfColumnsDP):
            listInitialize.append(0)
        dpMatrix.append(listInitialize[:])

    # Filling values in DP Matrix as per algorithm
    for i in range(numberOfRowsDP):

        for j in range(numberOfColumnsDP):

            if i == 0 or j == 0:
                dpMatrix[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                dpMatrix[i][j] = 1 + dpMatrix[i - 1][j - 1]

                # Storing new result if required
                if result[0] < dpMatrix[i][j]:
                    result = [ dpMatrix[i][j], (i, j) ]
                # Otherwise not changing the result
                else:
                    continue
            else:
                dpMatrix[i][j] = 0

    # Storing and getting longest common substring
    LongestCommonSubstring = string1[ result[1][0] - result[0] : result[1][0] ]

    # Printing DP Matrix
    print("\n\n Dynamic Programming Matrix  : \n\n")

    print("  #", end = " ")

    for chr in string2:
        print(chr, end = " ")

    print("\n")

    for i in range(numberOfRowsDP):
        if  i==0:
            print("#",end = " ")
        else:
            print(string1[i-1], end = " ")
        for j in range(numberOfColumnsDP):
                print(dpMatrix[i][j],end = " ")
        print("\n")

    # Printing result
    print("First string  : " + str(string1) + "\n")
    print("Second string : " + str(string2) + "\n")
    print("The longest common substring is : " + str(LongestCommonSubstring))
    print("The length of longest common subtring is : " + str(result[0]))



if __name__ == "__main__":
    main()
