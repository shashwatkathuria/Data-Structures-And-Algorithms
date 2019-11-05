# -*- coding: utf-8 -*-
"""
Created on Sat Nov  1 12:26:41 2019

@author: Shashwat Kathuria
"""

# Edit Distance Algorithm - Spell Checker


# Initializing required variables
closeWords = []
noOfCloseWordsRequired = 0

def main():
    global noOfCloseWordsRequired

    # Getting inputs
    inputWord = input("Enter input word : ")
    noOfCloseWordsRequired = int(input("Enter the number of close words required : "))

    # Opening dictionary file
    dictionaryFile = open("unix_word_list.dic", "r")

    n = 0
    # Comparing words for each word in dictionary file
    for line in dictionaryFile.readlines():
        print("Comparing...Please Wait...Compared " + str(n) + " words till now.")

        compareWord = line[:-1]
        # Calling edit distance algorithm
        editDistance(inputWord, compareWord)

        n += 1

    closeWords.sort()
    print("\n--------------\nANSWER\n--------------\n")
    # Printing the closest words
    for closeWord in closeWords:
        print("Word : {:30} Score : {:10} ".format(closeWord[1], closeWord[0]))


def editDistance(inputWord, compareString):
    """Function which implements Edit Distance Algorithm to find the "nearness"
       score of a input word to the one being compared with."""

    # Defining Penalties
    sameLetterPenalty = 0
    mismatchPenalty = 1
    gapMatchingPenalty = 2

    # Defining variables required
    m = len(inputWord) + 1
    n = len(compareString) + 1

    # Initializing DP Matrix
    dpMatrix = [[0 for j in range(n)] for i in range(m)]

    for i in range(m):
        dpMatrix.append([])
        for j in range(n):

            # Comparing empty string with corresponding substring
            if i == 0 or j == 0:
                dpMatrix[i][j] = (i + j) * gapMatchingPenalty

            # Comparing non empty substrings
            else:
                if inputWord[i - 1] == compareString[j - 1] or inputWord[i - 1].lower() == compareString[j - 1].lower():

                    # Both letters score
                    option1 = dpMatrix[i - 1][j - 1] + sameLetterPenalty
                    # Gap matching score
                    option2 = dpMatrix[i - 1][j] + gapMatchingPenalty
                    # Gap matching score
                    option3 = dpMatrix[i][j - 1] + gapMatchingPenalty

                    # Setting answer to the minimum of all three options
                    dpMatrix[i][j] = min(option1, option2, option3)

                elif inputWord[i - 1] != compareString[j - 1]:

                    # Both letters score
                    option1 = dpMatrix[i - 1][j - 1] + mismatchPenalty
                    # Gap matching score
                    option2 = dpMatrix[i - 1][j] + gapMatchingPenalty
                    # Gap matching score
                    option3 = dpMatrix[i][j - 1] + gapMatchingPenalty

                    # Setting answer to the minimum of all three options
                    dpMatrix[i][j] = min(option1, option2, option3)


    # Solution = dpMatrix[m - 1][n - 1]

    # Appending to close words if there are still empty spaces left in list
    if len(closeWords) < noOfCloseWordsRequired:
        closeWords.append((dpMatrix[m - 1][n - 1], compareString))
    # Appending to close words if better than the maximum in that list
    elif len(closeWords) == noOfCloseWordsRequired:
        if max(closeWords)[0] > dpMatrix[m - 1][n - 1]:
            closeWords[closeWords.index(max(closeWords))] = (dpMatrix[m - 1][n - 1], compareString)

# Calling main function
if __name__ == "__main__":
    main()
