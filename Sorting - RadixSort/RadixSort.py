# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:18:44 2017

@author: Shashwat Kathuria
"""

# RADIX SORT - USING COUNTING SORT

def main():

    # Reading elements from the input file and storing in an array
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        arr.append(int(file.readline()))

    # Printing input array
    print("\nThe input array looks as follows : \n\n" + str(arr) )

    # Calling radix sort algorithm on input array
    radixSort(arr)

    # Printing sorted array
    print("\nThe sorted array looks as follows : \n\n" + str(arr) )


def radixSort(arr):
    """Function to sort an array using radix sort algorithm. Input is the array to be sorted."""
    # Storing maximum element
    maxElement = max(arr)

    # Starting with rightmost digit of each number
    exponent = 1

    # Starting with exponent 1 as it will be divided with the corresponding array element
    # Therefore it wil give rightmost digit after computation, not the leftmost

    # Breaking loop if maximum digits required are exceeded
    while maxElement / exponent > 0:
        # Calling counting sort on the digit corresponding to variable exponent
        countingSort(arr,exponent)
        # Multiplying exponent by base 10 after each iteration
        exponent *= 10

def countingSort(arr,exponent):
    """Function to do counting sort on digits corresponding to exponent. Inputs are the
       array and exponent."""

    # Storing the variables required for storing temp array, count and number of elements in array
    noOfElements = len(arr)
    tempArr = [0] * noOfElements

    # Index 0 represents number of elements having corresponding digit 0,
    # Index 1 represents number of elements having corresponding digit 1, and so on
    count = [0] * 10

    # Incrementing the count of the digit encountered
    for i in range(noOfElements):
        count[ (arr[i] / exponent) % 10 ] += 1

    # Summing up the previous counts to get the appropriate positions to insert elements
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Inserting elements in appropriate positions
    for i in range(noOfElements - 1, -1, -1):
        index = arr[i] / exponent
        # The computation in bracket represents the appropriate position of element to be inserted in
        tempArr[ count[ index % 10] - 1] = arr[i]
        # Decrementing count by 1 as the element has been inserted
        count[index % 10] -= 1

    # Copying temp array to array
    for i in range(noOfElements):
        arr[i] = tempArr[i]

if __name__ == "__main__":
    main()
