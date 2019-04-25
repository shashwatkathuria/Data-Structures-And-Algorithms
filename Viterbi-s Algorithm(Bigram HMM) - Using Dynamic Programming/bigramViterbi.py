# -*- coding: utf-8 -*-

from __future__ import division
import codecs
from collections import defaultdict

def main():

    # Opening the input training file
    trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")

    # Getting the emission probabilities
    emissionProbabilityDict = calculateEmissionProbabilities(trainFile, 0.0, 0.000000001)

    # Opening the input training file
    trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")

    # Getting the transition probabilities and all the tags (states)
    transitionProbabilityDict, allTags = calculateTransitionProbabilities(trainFile, 0.0)

    # Opening the input file
    inputSentences = codecs.open("input.txt", mode = "r", encoding = "utf-8")

    # Initializing a list for sentences
    sentencesList = []

    # Reading the input file and storing the sentences
    for line in inputSentences:
        sentence = []
        tokens = line.split()
        for token in tokens:
            word = token.split('|')[0].strip()
            sentence.append(token)

        # Appending the sentence in the list of sentences
        sentencesList.append(sentence)

    print("\n===========================\nPRINTING THE RESULTS\n===========================\n")
    # Iterating through each of the sentences
    for sentence in sentencesList:

        # Calling the algorithm on the sentence
        predictedWordsAndTags = bigramHMMViterbiAlgorithm(sentence, allTags, emissionProbabilityDict, transitionProbabilityDict)
        print("\n=======\n")
        # Printing the result of the algorithm
        for (word, tag) in predictedWordsAndTags:
            print word, tag,
        print("\n")
    print("\n=========================\n")

def bigramHMMViterbiAlgorithm(sentence, allTags, emissionProbabilityDict, transitionProbabilityDict):

    # Appending a '*' required for the initial bigram in the algorithm(base case)
    sentence = [ u'*'] + sentence

    # Declaring the variables required
    initialLength = len(sentence)
    backtrackingDict = defaultdict(list)
    dpDict = {}
    tagsAssigned = []

    # Initializing the base cases
    dpDict[0, '*'] = 1
    for u in ([ u'*' ] + list(allTags)):
            if u != u'*':
                dpDict[0, u] = 1

    # Iterating through each word in the sentence from starting in terms of length
    for k in range(1, initialLength):
        # For all possibilities of (u, v) tags
        for v in allTags:

            # List for possibilities for getting maximum probability
            possibilities = []

            # For all possibilities of (u, v) tags
            for u in allTags:

                # Viterbi algorithm formula
                possibility = dpDict[k - 1 , u] * transitionProbabilityDict[(v, u)] * (emissionProbabilityDict[sentence[k] + '|' + v])

                # Appending the possibility to the list of possibilities
                possibilities.append((possibility, u))

            # Getting the maximum probability from the list of possibilities, element[0] is the probability of the possibility
            maxUVgivenK = max(possibilities, key = lambda element : element[0])

            # Storing the answer in the DP dict
            dpDict[k, v] = maxUVgivenK[0]

            # Getting the element to be backtracked and storing it in the backtracking Dict
            backtrackU = maxUVgivenK[1]
            backtrackingDict[v] += [backtrackU]

            # Additionally storing v of (u, v) tags in the last iteration
            if k == initialLength - 1:
                backtrackingDict[v] += [v]


    # List for getting the possibilities of final iterations
    maxPossibilitiesList = []

    for key in dpDict:

        # Getting the possibilities of the final iterations and appending to maxPossibilitiesList
        if (initialLength - 1 in key) and (dpDict[key] != 0):
            maxPossibilitiesList.append((key[1], dpDict[key]))

    # Finally getting the answer of the viterbi alogrithm, element[1] is the probability of the final iteration possibilities
    viterbiAnswer = max(maxPossibilitiesList, key = lambda element:element[1])

    # Getting the tags associated with the viterbiAnswer by referring to the backtrackingDP
    tagsAssigned = backtrackingDict[viterbiAnswer[0]][1:]

    # Removing the '*' appended in the starting of algorithm, not required anymore
    sentence = sentence[1:]

    # Returning the answer
    return zip(sentence, tagsAssigned)


def calculateTransitionProbabilities(trainFile, Lambda):

    # Declaring the variables and default dicts required
    transitionProbabilityDict = defaultdict(int)
    bigramTransitionCountDict = defaultdict(int)
    unigramTransitionCountDict = defaultdict(int)
    numberOfWords = 0
    numberOfSentences = 0
    allTags = set([])

    # Iterating through the lines of the input file
    for line in trainFile.readlines():

        # Getting tokens from each such line
        tokens = line.split()

        # Initializing a list for the tags observed in the line
        tags = []

        # For each token in that line
        for token in tokens:

            # Extracting the tag by splitting and stripping according to the file
            tag = token.split('|')[2].split('.')[0].strip(':?').strip()

            # Giving exact tags in training data a common parent tag for less complexity
            # and more accuracy
            if (tag == 'I-NP' or tag == 'B-NP' or tag == 'O'):
                tag = 'NN'

            allTags = allTags | set([tag])

            # Appending the tag to the list of tags
            tags.append(tag)

        # Incrementing the total number of words by the required amount
        numberOfWords += len(tags)

        # If the line read is not a blank line
        if tags != []:

            # Incrementing the total number of sentences by the required amount
            numberOfSentences += 1

            # Getting the unigrams in the exact order
            unigramSentenceList = tags[:]

            # Getting the bigrams in the exact order by zipping through the tags
            bigramSentenceList = zip(tags, tags[1:])

            # Incrementing the count of the unigrams as observed in the unigramSentenceList
            for unigram in unigramSentenceList:
                unigramTransitionCountDict[unigram] += 1

            # Incrementing the count of the unigrams as observed in the bigramSentenceList
            for bigram in bigramSentenceList:
                bigramTransitionCountDict[bigram] += 1

    # Calculating the transition probabilities finally
    # Iterating through the (u, v) bigrams
    for bigram in bigramTransitionCountDict:

        # Initializing variables as required
        uUnigram = bigram[0]
        vState = bigram[1]

        # Declaring the q(v | u) - transition probability
        keyVgivenU = (vState, uUnigram)

        # Calculating the transition probability
        transitionProbability = (bigramTransitionCountDict[bigram] + Lambda ) / (unigramTransitionCountDict[uUnigram] + (Lambda * (22 ** 2)))

        # Storing the transition probability in the dict
        transitionProbabilityDict[keyVgivenU] = transitionProbability

    # Printing the total number of words and sentences
    print("Total number of Words     : " + str(numberOfWords))
    print("Total number of Sentences : " + str(numberOfSentences))

    # Returning probability dict and tags set
    return transitionProbabilityDict, allTags


def calculateEmissionProbabilities(trainFile, Lambda, offset):

    # Declaring the variables and default dicts required
    # 0.000000001 as offset for smoothing
    emissionProbabilityDict = defaultdict(lambda : offset)
    emissionCountDict = defaultdict(int)
    separateTagCountDict = defaultdict(int)

    # Iterating through the lines of the input file
    for line in trainFile.readlines():

        # Getting tokens form each such line
        tokens = line.split()

        # Initializing a list for the tags observed in the line
        tags = []

        # For each token in that line
        for token in tokens:

                # Extracting the word by splitting and stripping according to the file
                word  = token.split('|')[0].strip()
                # Extracting the tag by splitting and stripping according to the file
                tag = token.split('|')[2].split('.')[0].strip(':?').strip()

                # Giving exact tags in training data a common parent tag for less complexity
                # and more accuracy
                if (tag == 'I-NP' or tag == 'B-NP' or tag == 'O'):
                    tag = 'NN'

                # Appending the tag to the list of tags
                tags.append(tag)

                # Calculating the number of times the tag and word appear together
                emissionCountDict[tag + '|' + word] += 1

                # Calculating the number of times that tag appears in general
                separateTagCountDict[tag] += 1

    # Iterating through the tag and word in the keys of emissionCountDict
    for key in emissionCountDict:

        # Getting the tag and word from the key
        tagAndWord = key.split('|')
        tag = tagAndWord[0]
        word = tagAndWord[1]

        # Calculating the emission probability
        emissionProbability = (emissionCountDict[tag + '|' + word] + Lambda ) / (separateTagCountDict[tag] + (Lambda * (22 ** 2)))

        # Storing the emission probability in the dict
        emissionProbabilityDict[word + '|' + tag] = emissionProbability

    # Returning probability dict
    return emissionProbabilityDict


if __name__ == "__main__":
    main()
