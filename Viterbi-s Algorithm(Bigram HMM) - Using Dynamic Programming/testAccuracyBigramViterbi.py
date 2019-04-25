# -*- coding: utf-8 -*-

# Importing the libraries and functions required
from __future__ import division
import codecs, time
from collections import defaultdict
from bigramViterbi import bigramHMMViterbiAlgorithm, calculateTransitionProbabilities, calculateEmissionProbabilities


def main():

    # CODE USED FOR CHECKING THE BEST VALUE OF LAMBDA AND OFFSET IS COMMENTED
    # AND THE BEST VALUES ARE USED

    # Lambdas = [0.00, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.10, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    # Offsets = [1, 0.1, 0.01, 0.001, 0.0001, 0.00001, 0.000001, 0.0000001, 0.00000001, 0.000000001, 0.0000000001, 0.00000000001, 0.000000000001]
    # offset = 0.000001
    Offsets = [1e-14]
    # for i in range(5):
        # Offsets.append(offset)
        # offset /= 100
    Lambdas = [0.04]
    for Lambda in Lambdas:
        for offset in Offsets:

            # Opening the input training file
            trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")

            # Getting the emission probabilities
            emissionProbabilityDict = calculateEmissionProbabilities(trainFile, Lambda, offset)

            # Opening the input training file
            trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")

            # Getting the transition probabilities and all the tags (states)
            transitionProbabilityDict, allTags = calculateTransitionProbabilities(trainFile, Lambda)

            # Opening the input test file
            testFile = codecs.open("testDataHindi.txt", mode = "r", encoding = "utf-8")

            # Calling the test function to get the accuracy of algorithm on the test data file
            accuracy = testBigramHMMViterbiAlgorithm(testFile, allTags, emissionProbabilityDict, transitionProbabilityDict, Lambda)

            # Printing the accuracy result
            print("============================")
            print("ACCURACY : " + str(accuracy) + " %" + " " + "Offset : " + str(offset) + " " + "Lambda : " + str(Lambda))
            print("============================")
            # print("Offset : " + str(offset))
            # print("Lambda : " + str(Lambda))
            time.sleep(5)

def testBigramHMMViterbiAlgorithm(testFile, allTags, emissionProbabilityDict, transitionProbabilityDict, Lambda):

    # Initializing the variables required for calculating accuracy
    totalTags = 0
    correctTags = 0

    # Reading the file line by line
    for line in testFile.readlines():

        # Getting tokens from each such line
        tokens = line.split()

        # Initializing a list for the words observed in the line
        sentence = []

        # Initializing a list for the tags observed in the line
        tags = []

        for token in tokens:

            # Extracting the word by splitting and stripping according to the file
            word = token.split('|')[0].strip()
            # Extracting the tag by splitting and stripping according to the file
            tag = token.split('|')[2].split('.')[0].strip(':?').strip()

            # Giving exact tags in training data a common parent tag for less complexity
            # and more accuracy
            if (tag == 'I-NP' or tag == 'B-NP' or tag == 'O'):
                tag = 'NN'

            # Appending the word to the list of words
            sentence.append(word)
            # Appending the tag to the list of tags
            tags.append(tag)

        # If the line read is not a blank line
        if sentence != []:

            # Zipping to get a list of (word, tag) tuple elements format
            actualWordsAndTags = zip(sentence, tags)

            try:
                # Calling the function on the sentence
                predictedWordsAndTags = bigramHMMViterbiAlgorithm(sentence, allTags, emissionProbabilityDict, transitionProbabilityDict)

                # Iterating through to compare the predicted and actual tags
                for i in range(len(sentence)):
                    actualTag = actualWordsAndTags[i][1]
                    predictedTag = predictedWordsAndTags[i][1]

                    # Incrementing the number of correct tags by 1 if it is such
                    if actualTag == predictedTag:
                        correctTags += 1

                    # Incrementing the number of total tags by 1
                    totalTags += 1

                    # Printing the results in between the interations
                    print "CORRECT TAGS : " + str(correctTags) + "  ======== " ,
                    print "TOTAL TAGS : " + str(totalTags)

            # A couple of lines in the file are arbitrary
            except:
                continue

    # Returning the result
    return (correctTags/totalTags) * 100

if __name__ == "__main__":
    main()
