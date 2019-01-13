# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 12:21:55 2017

@author: Shashwat Kathuria
"""

def main():
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        arr.append(int(file.readline()))
    print("\nThe input array is as follows : \n\n")
    print(arr)
    bubbleSort(arr)

def bubbleSort(arr):

    print("\n")

    for i in range(len(arr)):
        print("ON ITERATION NO : " + str(i) + " OUT OF " + str(len(arr)))
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]

    print("\n\nThe sorted array is as follows : \n\n")
    print(arr)
    print("\n")
    
if __name__ == "__main__":
    main()
