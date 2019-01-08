# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 15:17:15 2018

@author: Shashwat Kathuria
"""
import sys
counterReference = 0
def main():
    file = open("BigKnapsack.txt","r")
    knapsackInfo = file.readline().split(" ")
    noOfItems = int(knapsackInfo[1])
    capacity = int(knapsackInfo[0])
    counterReference = noOfItems
    weights = []
    values = []
    for i in range(noOfItems):
        tempItemInfo = file.readline().split(" ")
        weights.append(int(tempItemInfo[1]))
        print(i)
        values.append(int(tempItemInfo[0]))
    ans = {}

    sys.setrecursionlimit(10000)
    print(knapsackBig(ans, capacity, noOfItems, weights, values))

def knapsackBig(ans, size, noOfItems, weights, values):
    print("IN PROCESS...Please wait for counter to reach somewhere near " + str(counterReference) + "   : " + str(noOfItems)  )
    if noOfItems == 0 or size == 0:
        return 0
    if (noOfItems, size) in ans:
        return ans[(noOfItems, size)]

    if size < weights[noOfItems - 1]:
        optimalAnswer = knapsackBig(ans, size, noOfItems - 1, weights, values)
    else:
        optimalAnswer = max(knapsackBig(ans, size, noOfItems - 1, weights, values),
              knapsackBig(ans, size - weights[noOfItems - 1], noOfItems - 1, weights, values) + values[noOfItems - 1] )

    ans[(noOfItems, size)] = optimalAnswer
    return optimalAnswer

if __name__ == "__main__":
    main()
