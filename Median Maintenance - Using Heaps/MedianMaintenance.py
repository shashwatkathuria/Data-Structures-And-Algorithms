# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:39:35 2018

@author: Shashwat Kathuria
"""
def main():

    file = open("Median.txt", "r")

    noOfElements = int( file.readline() )
    listOfElements = []

    for i in range(noOfElements):
        element = int(file.readline()[:-1])
        listOfElements.append(element)

    print( noOfElements )
    print( listOfElements )

    minHeap = Heap( noOfElements, 30 )
    maxHeap = Heap( noOfElements, 30 )

    n1 = minHeap.getI()
    n2 = maxHeap.getI()

    medians = []
    medians.append( listOfElements[0] )
    medians.append( listOfElements[1] )

    minHeap.insertElement(-listOfElements[1], minHeap.getI())
    maxHeap.insertElement( listOfElements[0], maxHeap.getI())

    for i in range(2, noOfElements):
        print("CALCULATING.. CURRENTLY ON ITERATION NO "+ str(i) + " OUT OF " + str(noOfElements) )
        if n1 == n2:
            if listOfElements[i] < maxHeap.extractMinimum():
                minHeap.insertElement(-listOfElements[i], minHeap.getI())
                medians.append(-minHeap.extractMinimum())
                n1 += 1
            else:
                maxHeap.insertElement(listOfElements[i], maxHeap.getI())
                medians.append(maxHeap.extractMinimum())
                n2 += 1

        elif n1 == n2 + 1:
            if listOfElements[i] > ( minHeap.extractMinimum() * ( - 1 ) ):
                maxHeap.insertElement(listOfElements[i], maxHeap.getI())
                medians.append(-minHeap.extractMinimum())
                n2 += 1
            else:
                exchangeElementHeap = minHeap.extractMinimum() * ( - 1 )
                minHeap.removeMinimum()
                maxHeap.insertElement(exchangeElementHeap, maxHeap.getI())
                minHeap.insertElement(-listOfElements[i],minHeap.getI())
                medians.append(-minHeap.extractMinimum())
                n2 += 1

        elif n2 == n1 + 1:
            if listOfElements[i] < maxHeap.extractMinimum():
                minHeap.insertElement(-listOfElements[i], minHeap.getI())
                medians.append(-minHeap.extractMinimum())
                n1 += 1
            else:
                exchangeElementHeap = maxHeap.extractMinimum()
                maxHeap.removeMinimum()
                minHeap.insertElement(-exchangeElementHeap, minHeap.getI())
                maxHeap.insertElement(listOfElements[i], maxHeap.getI())
                medians.append(-minHeap.extractMinimum())
                n1 += 1


    print("\n\nThe sum of the medians over all the iterations is : " + str( sum(medians) ) + "\n\n")

class Heap:

    def __init__(self, noOfElements, limitOfRestructuring):
        self.heap = [ 'NaN' ] * noOfElements
        self.noOfElements = noOfElements
        self.i = 1
        self.noOfRemovedElements = 0
        self.limitOfRestructuring = limitOfRestructuring

    def __str__(self):
        string = "["
        for i in range(1, self.i , 1):
            string += str(self.heap[i]) + " "
        return string + "]"

    def extractMinimum(self):
        return self.heap[1]

    def getI(self):
        return self.i

    def insertElement(self, element , i ):
        self.heap[i] = element
        parenti = i // 2
        try:

            if parenti != 0 and self.heap[i] < self.heap[parenti]:
                self.heap[i], self.heap[parenti] = self.heap[parenti], self.heap[i]
                self.insertElement(element, parenti)
            else:
                self.i += 1
                return

        except:
            self.heap[i] = 'NaN'
            self.insertElement(element, parenti)
            return

    def removeMinimum(self, i = 1):

        if self.noOfRemovedElements == self.limitOfRestructuring:
            self.restructureHeap()
            self.noOfRemovedElements  = 0

        if self.heap[i] == 'NaN' :
            self.noOfRemovedElements += 1
            return
        if 2 * i + 1 > self.noOfElements or 2 * i > self.noOfElements:
            self.heap[i] == "NaN"
            self.noOfRemovedElements += 1
            return

        child1 = 2 * i
        child2 = ( 2 * i ) + 1

        if self.heap[child1] == 'NaN' and self.heap[child2] == 'NaN':
            self.heap[i] = 'NaN'
            self.noOfRemovedElements += 1
            return

        elif self.heap[child2] == 'NaN':
            self.heap[i], self.heap[child1] = self.heap[child1], "NaN"
            self.noOfRemovedElements += 1
            return

        elif self.heap[child1] == 'NaN':
            self.heap[i], self.heap[child2] = self.heap[child2], "NaN"
            self.noOfRemovedElements += 1
            return

        if self.heap[child1] <= self.heap[child2]:
            self.heap[i], self.heap[child1] = self.heap[child1], self.heap[i]
            self.removeMinimum( child1 )
        else:
            self.heap[i], self.heap[child2] = self.heap[child2], self.heap[i]
            self.removeMinimum( child2 )

    def restructureHeap(self):
        self.i = 1
        tempList = []
        for heapElement in self.heap:
            if heapElement != "NaN" :
                tempList.append( heapElement )
        self.heap = ["NaN"] * self.noOfElements
        for element in tempList:
            self.insertElement(element, self.i)

if __name__ == "__main__":
    main()
