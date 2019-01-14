# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:12:24 2017

@author: Shashwat Kathuria
"""

# SELECTION SORT

def main():

    # Reading input from the file and putting the elements in a list
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        number = int(file.readline())
        arr.append(number)

    # Printing the input lst
    print("\nThe input array is as follows : \n\n")
    print(arr)

    # Calling selection sort on the list
    selectionSort(arr)

def selectionSort(arr):
    """Selection Sort Algorithm function to sort an array.Input is the original array."""

    print("\n")

    # len(arr) - > n linear passes to sort the array
    for i in range(len(arr)):

        # Storing the position and element with which the smallest element
        # of the right unsorted subarray is to be exchanged
        print("ON ITERATION NUMBER : " + str(i + 1) + " OUT OF " + str(100000))
        position = i
        minimum = arr[i]

        # Finding the smallest element in the right unsorted subarray
        for j in range(i, len(arr), 1):
            if arr[j] <= minimum:
                position = j
                minimum = arr[j]

        # Exchanging the smallest element of the right unsorted array with
        # the element to the right of the left sorted subarray
        arr[i], arr[position] = minimum, arr[i]

    print("\n\nThe sorted array is as follows : \n\n")
    print(arr)
    print("\n")

if __name__ == "__main__":
    main()
