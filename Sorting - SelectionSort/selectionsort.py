# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 20:12:24 2017

@author: Shashwat Kathuria
"""

def main():
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        number = int(file.readline())
        arr.append(number)
    print("\nThe input array is as follows : \n\n")
    print(arr)

    selectionSort(arr)

def selectionSort(arr):

    print("\n")

    for i in range(len(arr)):
        print("ON ITERATION NUMBER : " + str(i + 1) + " OUT OF " + str(100000))
        position = i
        minimum = arr[i]
        for j in range(i, len(arr), 1):
            if arr[j] <= minimum:
                position = j
                minimum = arr[j]
        arr[i], arr[position] = minimum, arr[i]

    print("\n\nThe sorted array is as follows : \n\n")
    print(arr)
    print("\n")

if __name__ == "__main__":
    main()
