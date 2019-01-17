# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:59:15 2018

@author: Shashwat Kathuria
"""

# SMALL KNAPSACK - USING DYNAMIC PROGRAMMING (ITERATION)

def main():

    # Reading inputs from the file and storing them
    try:
        file = open("SmallKnapsack.txt","r")
    except:
        print("Could not open the file.Error")
        return

    # Storing knapsack info
    knapsackInfo = file.readline().split(" ")
    capacity = int(knapsackInfo[0])
    noofitems = int(knapsackInfo[1])

    # Storing available items info
    items = {}
    for i in range(noofitems):
        tempItemInfo = file.readline().split(" ")
        items[i + 1] = [ int(tempItemInfo[0]), int(tempItemInfo[1]) ]

    # Calling small knapsack algorithm
    answer = SmallKnapsack(noofitems, capacity, items)

    # Printing answer
    print("The optimal Knapsack solution is : " + str( answer[noofitems, capacity] ))

def SmallKnapsack(noofitems, capacity, items):
    """Function to compute optimal knapsack solution. Inputs are the capacity, number of items,
       and info about the items."""

    # Initializing base cases when number of items is zero
    dpMatrix = {}
    for x in range(capacity + 1):
        dpMatrix[0, x] = 0

    # Filling in values inside the DP Matrix
    for itemNo in range(1, noofitems + 1):
         print("ON ITEM NUMBER : " + str(itemNo))
         for x in range(capacity + 1):

             # Ignoring item if the weight of the item is bigger than the capacity of knapsack
             if items[itemNo][1] > x:
                 dpMatrix[itemNo, x] = dpMatrix[itemNo - 1, x]
                 continue
             # Considering the current item in knapsack
             a1 = dpMatrix[itemNo - 1, x]
             # Not considering the current item in the knapsack
             a2 = dpMatrix[itemNo - 1, x - items[itemNo][1]] + items[itemNo][0]
             # Storing the best of the two cases
             if a2 > a1:
                 dpMatrix[itemNo, x] = a2
             else:
                 dpMatrix[itemNo, x] = a1

    return dpMatrix


if __name__ == "__main__":
    main()
