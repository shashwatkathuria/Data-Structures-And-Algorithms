# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:17:15 2018

@author: Shashwat Kathuria
"""

# BIG KNAPSACK ALGORITHM - USING RECURSION AND DYNAMIC PROGRAMMING (MEMOIZATION)

# Extending recursion limit on system so that program does not give error
import sys
sys.setrecursionlimit(10000)

counterReference = 0

def main():
    global counterReference

    # Reading inputs from the input fie and storing them
    file = open("BigKnapsack.txt","r")
    knapsackInfo = file.readline().split(" ")
    noOfItems = int(knapsackInfo[1])
    capacity = int(knapsackInfo[0])

    counterReference = noOfItems

    # Storing info for all items
    weights = []
    values = []
    for i in range(noOfItems):
        tempItemInfo = file.readline().split(" ")
        weights.append(int(tempItemInfo[1]))
        print(i)
        values.append(int(tempItemInfo[0]))

    ans = {}
    # Calling knapsack algorithm
    print(knapsackBig(ans, capacity, noOfItems, weights, values))

def knapsackBig(ans, size, noOfItems, weights, values):
    """Funtion to compute optimal knapsack solution. Inputs are the info
       about knapsack, available items and a dict to store answers."""

    # Printing progress
    print("IN PROCESS...Please wait for counter to reach somewhere near " + str(counterReference) + "   : " + str(noOfItems)  )

    # Base case
    if noOfItems == 0 or size == 0:
        return 0

    # Memoization
    if (noOfItems, size) in ans:
        return ans[(noOfItems, size)]

    # if the weight of item is bigger than knapsack size, ignore that item
    if size < weights[noOfItems - 1]:
        optimalAnswer = knapsackBig(ans, size, noOfItems - 1, weights, values)
    # else compute the value once without considering that item and once considering that
    # item and store the maximum of the two
    else:
        optimalAnswer = max(knapsackBig(ans, size, noOfItems - 1, weights, values),
              knapsackBig(ans, size - weights[noOfItems - 1], noOfItems - 1, weights, values) + values[noOfItems - 1] )

    # Storing values for memoization
    ans[(noOfItems, size)] = optimalAnswer

    return optimalAnswer

if __name__ == "__main__":
    main()
