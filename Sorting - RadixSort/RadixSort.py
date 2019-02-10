# -*- coding: utf-8 -*-
"""
Created on Tue Feb 10 13:18:44 2017

@author: Shashwat Kathuria
"""
def main():
    file = open("IntegerArray.txt", "r")
    arr = []
    for i in range(100000):
        arr.append(int(file.readline()))
    print("\nThe input array looks as follows : \n\n" + str(arr) )

    radixSort(arr)

    print("\nThe sorted array looks as follows : \n\n" + str(arr) )


def radixSort(arr):

    maxElement = max(arr)

    exponent = 1

    while maxElement / exponent > 0:
        countingSort(arr,exponent)
        exponent *= 10

def countingSort(arr,exponent):

    noOfElements = len(arr)
    output = [0] * noOfElements
    count = [0] * 10

    for i in range(noOfElements):
        count[ (arr[i] / exponent) % 10 ] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(noOfElements - 1, -1, -1):
        index = arr[i] / exponent
        output[ count[ index % 10] - 1] = arr[i]
        count[index % 10] -= 1

    for i in range(noOfElements):
        arr[i] = output[i]

if __name__ == "__main__":
    main()
