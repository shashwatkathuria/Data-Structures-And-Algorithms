# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:04:18 2018

@author: Shashwat Kathuria
"""

# INSERTION SORT

def main():

    # Reading elements from the file and storing in a list
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        arr.append(int(file.readline()))
    print("\nThe input array looks as follows : \n\n" + str(arr) )

    # Calling insertion sort algorithm on the list
    insertionSort(arr)

def insertionSort(arr):
    """Insertion Sort Algorithm function to sort the array. Input is the list to be sorted."""
    print("\n")

    # len(arr) - 1 linear passes of the array to insert smallest element in the left sorted
    # subarray, starting from the 2nd element of the list
    for i in range(1, len(arr)):

        # Element to be inserted into the left sorted subarray
        element = arr[i]
        pos = i
        print("ON ITERATION NUMBER " + str(i) + " OUT OF : " + str(len(arr) - 1))

        # Calculating the position in which the element is to be inserted
        while arr[pos - 1] > element and pos!=0:
            pos -= 1

        # Bubbling element to the left  until it reaches the correct position
        for k in range(i , pos  , -1):
            arr[k], arr[k - 1] = arr[k - 1], arr[k]


    print("\n\nThe sorted array looks as follows : \n\n" +str(arr))
    print("\n")



if __name__ == "__main__":
    main()
