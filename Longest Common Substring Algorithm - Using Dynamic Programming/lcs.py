# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 12:54:12 2019

@author: Shashwat Kathuria
"""

def main():

    string1 = input( "Enter the first string : " )
    string2 = input( "Enter the second string : " )

    longestCommonSubstring(string1,string2)


def longestCommonSubstring(string1, string2):

    m = len(string1) + 1
    n = len(string2) + 1
    initialLcsDpPosition = (0, 0)
    result = [0, initialLcsDpPosition]

    dpMatrix = []
    for i in range(m):
        listInitialize = []
        for j in range(n):
            listInitialize.append(0)
        dpMatrix.append(listInitialize[:])

    for i in range(m):
        for j in range(n):
            if i == 0 or j == 0:
                dpMatrix[i][j] = 0
            elif string1[i - 1] == string2[j - 1]:
                dpMatrix[i][j] = 1 + dpMatrix[i - 1][j - 1]
                if result[0]<dpMatrix[i][j]:
                    result = [max(result[0], dpMatrix[i][j]),(i,j)]
                else:
                    continue
            else:
                dpMatrix[i][j] = 0

    LongestCommonSubstring = string1[ result[1][0] - result[0] : result[1][0] ]

    print("\n\n Dynamic Programming Matrix  : \n\n")

    print("  #", end = " ")

    for chr in string2:
        print(chr, end = " ")

    print("\n")

    for i in range(m):
        if  i==0:
            print("#",end = " ")
        else:
            print(string1[i-1], end = " ")
        for j in range(n):
                print(dpMatrix[i][j],end = " ")
        print("\n")

    print("First string  : " + str(string1))
    print("Second string : " + str(string2))
    print("The longest common substring is : " + str(LongestCommonSubstring))
    print("The length of longest common subtring is : " + str(result[0]))



if __name__ == "__main__":
    main()
