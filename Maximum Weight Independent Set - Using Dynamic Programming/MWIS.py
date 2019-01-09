# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 20:56:13 2018

@author: Shashwat Kathuria
"""
def main():
    file = open("MWIS.txt", "r")
    noOfNodes = int(file.readline())
    weights = {}
    for i in range( noOfNodes ):
        weights[ i + 1 ] = int( file.readline() )

    MWIS(weights, noOfNodes)

def MWIS(weights, noOfNodes):
    ans = [ 0 ] * ( noOfNodes + 1 )
    ans[1] = weights[1]
    for i in range(2, noOfNodes + 1):
        a1 = ans[ i - 1 ]
        a2 = ans[ i - 2 ] + weights[i]
        if a1 > a2:
            ans[i] = a1
        else:
            ans[i] = a2
    nodesSelected = []
    i = noOfNodes
    while i > 0:
        if i != 1:
            a1 = ans[ i - 1 ]
            a2 = ans[ i - 2 ] + weights[i]
            if a2 > a1:
                nodesSelected.append(i)
                i -= 2
            else:
                i -= 1

        if i == 1:
            nodesSelected.append(i)
            i -= 1
    nodesSelected.sort()
    print("The following nodes are a part of the maximum weight independent set : \n\n" + str(nodesSelected) )
    print("\nThe optimal solution to the maximum weight independent set is : " + str(ans[noOfNodes]) )

if __name__ == "__main__":
    main()
