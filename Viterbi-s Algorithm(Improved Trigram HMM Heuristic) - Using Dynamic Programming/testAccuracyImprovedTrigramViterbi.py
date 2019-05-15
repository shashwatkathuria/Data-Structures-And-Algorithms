# -*- coding: utf-8 -*-

from __future__ import division
import codecs, time
from collections import defaultdict
from improvedTrigramViterbi import trigramHMMViterbiAlgorithm, calculateTransitionProbabilities, calculateEmissionProbabilities


def main():

    # CODE USED FOR CHECKING THE BEST VALUE OF LAMBDA,WEIGHT AND OFFSET IS COMMENTED
    # AND THE BEST VALUES ARE USED

    # Lambdas = [0.1, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
    Lambdas = [0.00]
    # lambda1 = 0
    # for i in range(10):
    #     Lambdas.append(lambda1)
    #     lambda1 += 0.1
    # offset = 0.000001
    # Offsets = []
    # for i in range(6):
    #     Offsets.append(offset)
    #     offset /= 100
    # Weights = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    Offsets = [1e-14]
    Weights = [9]
    for Lambda in Lambdas:
        for offset in Offsets:
            for weight in Weights:

                # Opening the input training file
                trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")

                # Getting the emission probabilities
                emissionProbabilityDict = calculateEmissionProbabilities(trainFile, Lambda, offset)

                # Opening the input training file
                trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")

                # Getting the transition probabilities and all the tags (states)
                transitionProbabilityDict, allTags = calculateTransitionProbabilities(trainFile, Lambda, weight)

                # Opening the input test file
                testFile = codecs.open("testDataHindi.txt", mode = "r", encoding = "utf-8")

                # Calling the test function to get the accuracy of algorithm on the test data file
                accuracy = testTrigramHMMViterbiAlgorithm(testFile, allTags, emissionProbabilityDict, transitionProbabilityDict)

                # Printing the accuracy result
                print("============================")
                print("ACCURACY : " + str(accuracy) + " %" + " " + "Offset : " + str(offset) + " " + "Lambda : " + str(Lambda) + " " + "Weight : " + str(weight))
                print("============================")
                time.sleep(1)

def testTrigramHMMViterbiAlgorithm(testFile, allTags, emissionProbabilityDict, transitionProbabilityDict):

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

            # Appending the word to the list of word
            sentence.append(word)
            # Appending the tag to the list of tags
            tags.append(tag)

        # If the line read is not a blank line
        if sentence != []:

            # Zipping to get a list of (word, tag) tuple elements format
            actualWordsAndTags = zip(sentence, tags)

            try:
                # Calling the function on the sentence
                predictedWordsAndTags = trigramHMMViterbiAlgorithm(sentence, allTags, emissionProbabilityDict, transitionProbabilityDict)

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
                print("Couldn't Tag Sentence")
                continue

    # Returning the result
    return (correctTags/totalTags) * 100

if __name__ == "__main__":
    main()
