# -*- coding: utf-8 -*-
"""
Created on Thu Nov 22 01:03:09 2018

@author: Shashwat Kathuria
"""

# FRACTIONAL KNAPSACK - GREEDY ALGORITHM

def main():

    # Reading inputs from the file and storing info about items
    file = open("input.txt", "r")
    size = int( file.readline() )
    noOfItems = int( file.readline() )

    # Declaring empty lists for weights and values
    weights = []
    values = []
    for i in range(noOfItems):
        itemInfo = file.readline().split(" ")
        values.append( int(itemInfo[0]) )
        weights.append( int(itemInfo[1]) )

    # Declaring empty lists for ratio
    ratios = []
    for i in range(noOfItems):
        ratios.append( [values[i] / weights[i], weights[i], i + 1] )

    # Calling fractional knapsack algorithm on items
    fractionalKnapsack(size, ratios)

def fractionalKnapsack(size, ratios):
    """Fractional Knapsack Algorithm function to compute the maximum value
       from a given set of items subject to a given size."""\

    # Sorting items in decreasing order of their ratios
    ratios.sort(reverse = True)
    ans = 0
    # Items selected by algorithm, optimum solution
    itemsSelected = []

    # Declaring item number counter
    itemNo = 0

    # Loop to run till there is possible space left in the knapsack
    while size > 0 :

        # If there is space left after putting the current item in the knapsack
        if size - ratios[itemNo][1] >= 0:
            # Add current item to the items selected
            itemsSelected.append( ratios[itemNo][2] )
            # Add the value of item to the ans (weight * ratio)
            ans += ( ratios[itemNo][1] * ratios[itemNo][0] )
            # Deduct the item weight from the size
            size -= ratios[itemNo][1]
        # Else chose a fraction of the item and terminate the algorithm
        else:
            # Computing fraction that is possible to be added
            fraction = size / ratios[itemNo][1]
            # Adding the current item to the items selected
            itemsSelected.append( ratios[itemNo][2] )
            # Add the fractional value of the item to the ans (fraction * (weight * ratio))
            ans += ( fraction * ( ratios[itemNo][1] * ratios[itemNo][0] ) )
        # Increment item number for next item
        itemNo += 1

    # Printing the items selected and the optimum value of the knapsack
    itemsSelected.reverse()
    print( "The items selected are : " + str( itemsSelected ) )
    print( "The optimal knapsack solution is : " + str( ans ) )

if __name__ == "__main__":
    main()
