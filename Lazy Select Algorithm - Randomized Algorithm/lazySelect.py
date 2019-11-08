# -*- coding: utf-8 -*-
"""
Created on Sat Nov 3 13:56:31 2019

@author: Shashwat Kathuria
"""

# Lazy Select Algorithm

# Importing required library
import random
N = None

def main():
    global N
    # Reading input file of 1-N numbers each distinct and appears once exactly
    inputFile = open("LazySelectInput.txt", "r")
    arr = []
    for line in inputFile.readlines():
        arr.append(int(line[:-1]))

    N = len(arr)

    choice = int(input("Enter 0 to analyze/test correctness and 1 to give your own specific input k : "))

    # Analyzing Correctness and Testing
    if choice == 0:
        onepass = 0
        numberOfPasses = 0
        successPasses = 0
        for k in range(1, N + 1):
            # Function runs until it yields a correct answer, initialized to "Fail"
            ans = "Fail"


            # Loop runs until correct answer is found
            for i in range(1000):

                # Calling lazy select algorithm
                ans = lazySelect(arr, k)

                numberOfPasses += 1
                if ans != "Fail":
                    if i == 0:
                        onepass += 1
                    successPasses += 1
                    break

            # Printing answer
            if ans != "Fail":
                print("The k(" + str(k) + ")th smallest number in the array is : " + str(ans))
            else:
                print("Maximum number of runs exceeded. Algorithm failed to produce correct output.")
        print("Number of one pass result return : " + str(onepass))
        print("Number of mean passes result return : " + str(numberOfPasses / N))
        print("Probability of succeding in onepass : " + str(onepass / N))
        print("Probability of success : " + str(successPasses / N))
        print("Probability of bound of success ( 1 - O( n ** (-1/4) ) ) is >= " + str(1 - ((N ** (-1/4)))))

    # Running for specific input
    else:
        # Taking input
        k = int(input("Enter the value of k (kth smallest number) : "))

        # Checking for input correctness
        if k > len(arr) or k <= 0:
            print("Wrong Input.")
        else:
            # Function runs until it yields a correct answer, initialized to "Fail"
            ans = "Fail"
            # Loop runs until correct answer is found
            for i in range(1000):

                # Calling lazy select algorithm
                ans = lazySelect(arr, k)

                if ans != "Fail":
                    break

            # Printing answer
            if ans != "Fail":
                print("The k(" + str(k) + ")th smallest number in the array is : " + str(ans))
            else:
                print("Maximum number of runs exceeded. Algorithm failed to produce correct output.")

def lazySelect(arr, k):
    """Function which implements Lazy Select Algorithm to find kth smallest number of a sequence."""

    # Corner cases to fasten algorithm
    if k == len(arr):
        return max(arr)
    elif k == 1:
        return min(arr)

    # Initializing required variables
    length = len(arr)
    n3by4 = int(length ** (3 / 4))
    n1by2 = length ** (1 / 2)

    # Uniformly randomly choosing n ** (3 / 4) elements from the input array
    R = random.sample(arr, n3by4)

    # Initializing require variables
    x = int((k / length) * (length ** (3 / 4)))

    l = int(max(x - n1by2, 0))
    h = int(min(x + n1by2, n3by4 - 1))

    # Indexing the randomly chosen subarray
    L = R[l]
    H = R[h]

    # Required variables for algorithm
    lPosition = 0
    hPosition = 0

    # Final set to be sorted and elements to be appended in this
    P = []

    # Incrementing lPosition and hPosition and appending elements to P if required
    for i in range(length):
        if arr[i] < L:
            lPosition += 1
        if arr[i] < H:
            hPosition += 1
        if arr[i] >= L and arr[i] <= H:
            P.append(arr[i])

    # Returning answer if conditions are satisfied
    if lPosition <= k and k <= hPosition and len(P) <= 4 * n3by4 + 1:
        # Sorting P and returning answer
        P.sort()
        position = k - lPosition - 1
        if position >= 0:
            return P[k - lPosition - 1]
        else:
            return "Fail"

    # Otherwise algorithm fails
    else:
        return "Fail"

# Calling main function
if __name__ == "__main__":
    main()
