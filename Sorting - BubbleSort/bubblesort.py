# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:21:55 2017

@author: Shashwat Kathuria
"""

# BUBBLE SORT

def main():

    # Reading file and storing elements in a list
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        arr.append(int(file.readline()))
    print("\nThe input array is as follows : \n\n")
    print(arr)

    # Calling bubble sort algorithm on list
    bubbleSort(arr)

def bubbleSort(arr):
    """"Bubble Sort Algortihm to sort an array. Input is the list to be sorted."""

    print("\n")

    # Iterating through array
    for i in range(len(arr)):

        # Defining variabble swap for efficient termination if possible
        swap = False
        print("ON ITERATION NO : " + str(i) + " OUT OF " + str(len(arr)))

        # Swapping adjacent elements if required
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                swap = True
                arr[j], arr[i] = arr[i], arr[j]

        # Breaking early if no swaps are encountered
        if swap == False:
            break
    print("\n\nThe sorted array is as follows : \n\n")
    print(arr)
    print("\n")

if __name__ == "__main__":
    main()
