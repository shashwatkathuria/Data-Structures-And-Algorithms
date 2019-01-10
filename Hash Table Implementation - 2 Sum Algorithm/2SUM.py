# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 14:30:13 2018

@author: Shashwat Kathuria
"""
hashTable = [ [0] ] * 111827

def main():

    file = open("2SUM.txt", "r")

    listOfElements = []
    for i in range(1000000):
        element = int( file.readline() )
        listOfElements.append([element, hashFunction(element)])
        print("READING ELEMENT NUMBER " + str(i + 1))


    for i in range(1000000):
        print("INSERTING ELEMENT NUMBER " + str(i + 1))

        temp = []
        temp = ( hashTable[listOfElements[i][1]] ) [ : ]

        if listOfElements[i][0] not in temp:
            temp.append(listOfElements[i][0])
            hashTable[listOfElements[i][1]] = temp[:]

    print("\n\nANALYZING THE DISTRIBUTION OF ELEMENTS IN HASH TABLE:-\n\n")

    ctr = 0
    for i in hashTable:
        ctr+=1
        print("Length of the list number " + str(ctr) + " in hash table is " + str( len(i) ) )


    i = 0
    answer = []
    for sum in range(-10000, 10000+1):
        print("COMPUTING ON SUM : " + str(sum))
        for element in  listOfElements:
            otherElement = sum - element[0]
            hashCalc = hashFunction(otherElement)
            flag = False
            for hashElement in hashTable[ hashCalc ]:
                if hashElement == otherElement:
                    i += 1
                    answer.append(sum)
                    print("=> " + str(sum) + " SATISFIES THE 2 Sum PROPERTY")
                    print("=> Total number of sums satisfying the 2 Sum property till now is : " + str(i))
                    flag = True
                    break
            if flag == True:
                break

    print("\nThe following sums satisfy the 2 Sum property : \n" + str(answer))
    print("\nThe total number of sums satisfying 2 SUM property is : " + str(i) + "\n\n")

def hashFunction(number):
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
