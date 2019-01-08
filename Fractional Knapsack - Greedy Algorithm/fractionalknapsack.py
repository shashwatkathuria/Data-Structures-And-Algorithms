# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 01:03:09 2018

@author: Shashwat Kathuria
"""

def main():

    file = open("input.txt", "r")
    size = int( file.readline() )
    noOfItems = int( file.readline() )

    weights = []
    values = []
    for i in range(noOfItems):
        itemInfo = file.readline().split(" ")
        values.append( int(itemInfo[0]) )
        weights.append( int(itemInfo[1]) )

    ratios = []
    for i in range(noOfItems):
        ratios.append( [values[i] / weights[i], weights[i], i + 1] )
    ratios.sort()
    ratios.reverse()
    ans = 0
    items = []
    j = 0
    while size > 0 :
        if size - ratios[j][1] >= 0:
            items.append( ratios[j][2] )
            ans += ( ratios[j][1] * ratios[j][0] )
            size -= ratios[j][1]
        else:
            fraction = size / ratios[j][1]
            items.append( ratios[j][2] )
            ans += ( fraction * ( ratios[j][1] * ratios[j][0] ) )
        j += 1
    items.sort()
    print( "The items selected are : " + str( items ) )
    print( "The optimal knapsack solution is : " + str( ans ) )

if __name__ == "__main__":
    main()
