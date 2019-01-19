# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 20:56:13 2018

@author: Shashwat Kathuria
"""


# MAXIMUM WEIGHT INDEPENDENT SET ALGORITHM (FOR PATH GRAPHS) - USING DYNAMIC PROGRAMMING
def main():

    # Reading from the input file and storing information weight of the nodes
    file = open("MWIS.txt", "r")
    noOfNodes = int(file.readline())
    weights = {}
    for i in range( noOfNodes ):
        weights[ i + 1 ] = int( file.readline() )

    # Calling maximum weight independent set algorithm on the path graph
    MWIS(weights, noOfNodes)

def MWIS(weights, noOfNodes):

    # Declaring answer list
    ans = [ 0 ] * ( noOfNodes + 1 )

    # Initializing answer list
    ans[1] = weights[1]
    # Running for loop for referring to previous answers and storing new ones
    for i in range(2, noOfNodes + 1):

        # Option 1 - Not including current ith vertex in MWIS
        a1 = ans[ i - 1 ]
        # Option 2 - Including current ith vertex in MWIS
        a2 = ans[ i - 2 ] + weights[i]

        # Storing bigger of two answers
        if a1 > a2:
            ans[i] = a1
        else:
            ans[i] = a2

    # Declaring list for storing the nodes selected in the MWIS
    nodesSelected = []
    i = noOfNodes

    # Backtracking to get the nodes selected
    while i > 0:
        if i != 1:
            # Option 1 - Not including current ith vertex in MWIS
            a1 = ans[ i - 1 ]
            # Option 2 - Including current ith vertex in MWIS
            a2 = ans[ i - 2 ] + weights[i]

            # Storing the ith vertex if it is bigger than the other option
            # and correspondingly decrementing the value of list position
            # counter i
            if a2 > a1:
                nodesSelected.append(i)
                i -= 2
            # Else not storing and continuing with the previous
            else:
                i -= 1

        # Abnormal case to get around i - 2 element of list, i.e , the last element,
        # which was not to be analyzed
        if i == 1:
            nodesSelected.append(i)
            i -= 1

    # Sorting list
    nodesSelected.reverse()

    # Printing result
    print("The following nodes are a part of the maximum weight independent set : \n\n" + str(nodesSelected) )
    print("\nThe optimal solution to the maximum weight independent set is : " + str(ans[noOfNodes]) )

if __name__ == "__main__":
    main()
