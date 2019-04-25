# -*- coding: utf-8 -*-

from __future__ import division
import codecs
from collections import defaultdict

def main():
    trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")
    emissionProbabilityDict = calculateEmissionProbabilities(trainFile)
    trainFile = codecs.open("trainDataHindi.txt", mode = "r", encoding = "utf-8")
    transitionProbabilityDict = calculateTransitionProbabilities(trainFile)
    # for key in transitionProbabilityDict:
    #     print(key,transitionProbabilityDict[key])

def calculateTransitionProbabilities(trainFile):

    transitionProbabilityDict = defaultdict(int)
    trigramTransitionCountDict = defaultdict(int)
    bigramTransitionCountDict = defaultdict(int)
    s = 0
    s1 = 0
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

            # Appending the tag to the list of tags
            tags.append(tag)

        s += len(tags)
        # print(tags)

        # If the line read is not a blank line
        if tags != []:
            s1+=1
            # Getting the bigrams in the exact order by zipping through the tags
            bigramSentenceList = zip(tags,tags[1:])

            # Getting the trigrams in the exact order by zipping through the tags
            trigramSentenceList = zip(tags, tags[1:], tags[2:])
            # print(bigramSentenceList)
            # print(trigramSentenceList)

            for bigram in bigramSentenceList:
                # print(bigram)
                bigramTransitionCountDict[bigram] += 1
                # print(bigramTransitionCountDict[bigram])

            for trigram in trigramSentenceList:
                # print(trigram)
                trigramTransitionCountDict[trigram] += 1
                # print(trigramTransitionCountDict[trigram])

    # Calculating the transition probabilities finally
    for trigram in trigramTransitionCountDict:
        uvBigram = trigram[:-1]
        sState = (trigram[-1],)
        keySgivenUV = sState + uvBigram
        # print(trigram, trigramTransitionCountDict[trigram])
        # print(uvBigram, bigramTransitionCountDict[bigram])
        transitionProbability = trigramTransitionCountDict[trigram] / bigramTransitionCountDict[bigram]
        # print(keySgivenUV, transitionProbability)
        transitionProbabilityDict[keySgivenUV] = transitionProbability

    # print("----------------------")
    # s = 0
    # for key in transitionProbabilityDict:
    #     s+=1
    #     print(key,transitionProbabilityDict[key])
    print("Number of Words     : " + str(s))
    print("Number of Sentences : " + str(s1))
    return transitionProbabilityDict


def calculateEmissionProbabilities(trainFile):

    emissionProbabilityDict = defaultdict(int)
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


    for key in emissionCountDict:

        tagAndWord = key.split('|')
        tag = tagAndWord[0]
        word = tagAndWord[1]
        emissionProbability = emissionCountDict[tag + '|' + word] / separateTagCountDict[tag]
        emissionProbabilityDict[word + '|' + tag] = emissionProbability

    return emissionProbabilityDict


if __name__ == "__main__":
    main()
