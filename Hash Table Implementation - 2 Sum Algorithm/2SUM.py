# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:30:13 2018

@author: Shashwat Kathuria
"""

# 2 - SUM ALGORITHM - USING HASH TABLE IMPLEMENTATION

# Defining a hashTable of such a size so as to minimize
# arbitrary insertions like, only even buckets are filled, etc
hashTable = [ [0] ] * 111827 # Prime number not close to a power of 2 or 10

def main():

    # Reading input elements from file and storing them inside a list,along with their hash function values
    file = open("2SUM.txt", "r")

    listOfElements = []
    print("READING ELEMENTS FROM THE FILE..PLEASE WAIT ")
    for i in range(1000000):
        element = int( file.readline() )
        listOfElements.append( [element, hashFunction(element)] )

    # Separate chaining the hash table using a quick and dirty hash function
    print("INSERTING ELEMENTS INTO THE HASH TABLE..PLEASE WAIT ")
    for i in range(1000000):
        temp = []
        temp = ( hashTable[listOfElements[i][1]] ) [ : ]

        if listOfElements[i][0] not in temp:
            temp.append(listOfElements[i][0])
            hashTable[listOfElements[i][1]] = temp[:]

    # Printing the length of all chains in the hash table to analyze whether they
    # are close-to-evenly distributed or not
    print("\n\nANALYZING THE DISTRIBUTION OF ELEMENTS IN HASH TABLE:-\n\n")

    ctr = 0
    for i in hashTable:
        ctr += 1
        print("Length of the list number " + str(ctr) + " in hash table is " + str( len(i) ) )

    ## 2 - SUM ALGORITHM
    i = 0
    answer = []
    # iterating through all the sums
    for sum in range(-10000, 10000+1):

        print("COMPUTING ON SUM : " + str(sum))

        # Searching for an element in the list of input elements to satisfy the 2 - SUM property
        for element in  listOfElements:

            # corresponding element which should exist in the hash table if satisfying the property
            otherElement = sum - element[0]
            hashCalc = hashFunction(otherElement)
            flag = False

            # Searching for the corresponding element in the chain of the hash table where it
            # should be present if it satisfies the 2 - SUM property
            for hashElement in hashTable[ hashCalc ]:
                if hashElement == otherElement:
                    i += 1
                    answer.append(sum)
                    print("=> " + str(sum) + " SATISFIES THE 2 Sum PROPERTY")
                    print("=> Total number of sums satisfying the 2 Sum property till now is : " + str(i))
                    flag = True
                    break
            # If any such element exists, we move on to the next sum
            if flag == True:
                break

    # Printing the results
    print("\nThe following sums satisfy the 2 Sum property : \n" + str(answer))
    print("\nThe total number of sums satisfying 2 SUM property is : " + str(i) + "\n\n")

def hashFunction(number):
    """Quick and Dirty Hash Function to compute the hash value of an element and then return
       modulus of the element with the hash tale size.Input is the hash value of the element to be
       obtained."""

    # Some random type operations
    if number < 0:
        number = abs( number )
        number += 17
    str1 = str( number )
    remainder = number % 17
    ans = ""
    for i in range( len(str1) ):
        if i % 2 == 0:
            ans += str1[i]
    ans += str( remainder )
    return int(ans) % 111827

if __name__ == "__main__":
    main()
