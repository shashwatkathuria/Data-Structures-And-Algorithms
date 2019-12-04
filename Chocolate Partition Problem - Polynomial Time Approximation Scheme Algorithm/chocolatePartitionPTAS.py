# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 20:56:13 2019

@author: Shashwat Kathuria
"""

# Chocolate Partition Problem PTAS Algorithm
# PTAS = Polynomial Time Approximation Scheme

# Importing required libraries
from itertools import combinations
import time

def main():

    # Opening input file
    inputFile = open("input.txt")

    # Getting epsilon approximation bound input
    E = float(input("Enter the value of parameter 0<E<1 for the algorithm : "))
    if E <= 0 or E >= 1:
        print("Invalid input.")
        return
    # Reading and storing input
    chocolates = []
    i = 1
    for line in inputFile.readlines():
        chocolates.append((i, int(line.strip(" "))))
        i += 1
    chocolates.sort(reverse = True, key = lambda element: element[1])

    # Printing approximate PTAS solution
    print("--------------------------------")
    print("APPROXIMATE PTAS SOLUTION FOR E = " + str(E))
    print("--------------------------------")
    approximateA, approximateB = chocolatePartitionPTAS(chocolates, E)
    sumA = chocolateSum(approximateA)
    sumB = chocolateSum(approximateB)
    # Sorting for better presentation
    approximateA.sort(key = lambda element : element[0])
    approximateB.sort(key = lambda element : element[0])
    print("\nApproximate Set A : -> Format(Chocolate Number, Chocolate Weight)\n\n" + str(approximateA))
    print("\nApproximate Set B : -> Format(Chocolate Number, Chocolate Weight)\n\n" + str(approximateB))
    print("Set A Sum : ", sumA)
    print("Set B Sum : ", sumB)
    print("Difference: ", abs(sumA - sumB))
    print("--------------------------------")

    # Comparing running times for different E values
    print("COMPARING RUNNING TIME FOR DIFFERENT VALUES OF E")
    print("--------------------------------")

    # Choosing a set of appropriate values for comparison
    for e in [0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.12, 0.14, 0.16, 0.18, 0.2, 0.3, 0.4]:

        # Running algorithm for each and outputing time taken
        start = time.time()
        chocolatePartitionPTAS(chocolates, e)
        end = time.time()
        print("Time taken by e = " + str(e) + " is " + str(round(end - start, 7)) + " seconds.")

    print("\nWe can see that the values are a function of n^1/e in comparison.")
    print("--------------------------------")

def chocolatePartitionPTAS(chocolates, E):
    """Function for the polynomial time approximation algorithm
       of the chocolate partition problem. Assuming chocolate weights
       are in decreasing order"""

    # Defining m to be the limit of optimal sub solution
    m = int(1/E)

    # Getting optimal solution of chocolates 1 to m
    A, B = chocolatePartitionOptimal(chocolates[:m][:])

    # Approximating solution for m + 1 to n chocolates
    for chocolate in chocolates[m : ]:
        # Balancing weights whenever set overweighs the other
        if chocolateSum(A) <= chocolateSum(B):
            A.append(chocolate)
        else:
            B.append(chocolate)

    # Returning the approximate solution
    return A, B

def chocolatePartitionOptimal(chocolates):
    """Function for the optimal solution of the
       chocolate partition problem."""

    # Variables to keep track of optimal solution during iterations
    min = None
    minA = None
    minB = None
    s = chocolates
    for combs in (combinations(s, r) for r in range(len(s)+1))  :
        for comb in combs:

            # Set A
            A = list(comb)
            # Set B = Universe - Set B
            B = list(set(s[:]) - set(comb))

            # If there is no minimum yet
            if min == None:
                # Storing the first value
                min = abs(chocolateSum(A) - chocolateSum(B))
                minA = A[:]
                minB = B[:]
            # If minimum exists
            else:
                # Store new value if only it is smaller than the current value
                if abs(chocolateSum(A) - chocolateSum(B)) < min:
                    # Storing new minimum values
                    min = abs(chocolateSum(A) - chocolateSum(B))
                    minA = A[:]
                    minB = B[:]

    # Sorting for better presentation
    minA.sort(key = lambda element : element[0])
    minB.sort(key = lambda element : element[0])

    # Returning answer
    return minA, minB

def chocolateSum(chocolates):
    """Function to return the sum of all the chocolate weights
       in the input chocolates list."""

    # Iterating and incrementing sum by chocolate weights
    sum = 0
    for chocolate in chocolates:
        sum += chocolate[1]

    # Returning sum
    return sum

# Calling main function
if __name__ == "__main__":
    main()
