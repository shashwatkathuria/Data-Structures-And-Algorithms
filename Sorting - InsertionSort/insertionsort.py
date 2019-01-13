# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:04:18 2018

@author: Shashwat Kathuria
"""

def main():

    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        arr.append(int(file.readline()))
    print("\nThe input array looks as follows : \n\n" + str(arr) )

    insertionSort(arr[:10])

def insertionSort(arr):

    print("\n")

    for i in range(1, len(arr)):
        element = arr[i]
        pos = i
        print("ON ITERATION NUMBER " + str(i) + " OUT OF : " + str(len(arr) - 1))

        while arr[pos - 1] > element and pos!=0:
            pos -= 1

        for k in range(i , pos  , -1):
            arr[k], arr[k - 1] = arr[k - 1], arr[k]


    print("\n\nThe sorted array looks as follows : \n\n" +str(arr))
    print("\n")



if __name__ == "__main__":
    main()
