# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 18:39:35 2018

@author: Shashwat Kathuria
"""

# MEDIAN MAINTENANCE USING HEAPS

def main():

    # Reading input elements from the file and storing in a list
    file = open("Median.txt", "r")

    noOfElements = int( file.readline() )
    listOfElements = []

    for i in range(noOfElements):
        element = int(file.readline()[:-1])
        listOfElements.append(element)

    # Printing the number of input elements and input array containing them
    print( noOfElements )
    print( listOfElements )

    # Declaring two heaps for median maintenance

    # min heap stores left smaller half, min here means storing smaller elements
    # and having root as the maximum element, which is contrary to convention
    minHeap = Heap( noOfElements, 30 )

    # max heap stores right bigger half, max here means storing bigger elements
    # and having root as the minimum element, which is contrary to convention
    maxHeap = Heap( noOfElements, 30 )

    # n1 and n2 keep track of the number of elements in the heaps
    # to be used when insering or replacing elements into or from the heaps
    n1 = minHeap.getI()
    n2 = maxHeap.getI()

    # list to store the median in each iteration
    medians = []

    # Base cases storage
    medians.append( listOfElements[0] )
    medians.append( listOfElements[1] )

    # Base cases storage
    minHeap.insertElement(-listOfElements[1], minHeap.getI())
    maxHeap.insertElement( listOfElements[0], maxHeap.getI())

    # for loop n - 2 times for getting median at each iteration
    # 2 times already done in base cases
    for i in range(2, noOfElements):

        print("CALCULATING.. CURRENTLY ON ITERATION NO "+ str(i) + " OUT OF " + str(noOfElements) )
        # various conditions to get the median, which is the
        # root of the minheap

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

    # Printing answer, i.e, the sum of the medians
    print("\n\nThe sum of the medians over all the iterations is : " + str( sum(medians) ) + "\n\n")

class Heap:

    def __init__(self, noOfElements, limitOfRestructuring):
        """"Initializes heap instance.Inputs are no of elements in heap and limit of restructuring of heap."""

        self.heap = [ 'NaN' ] * noOfElements
        self.noOfElements = noOfElements
        self.i = 1
        self.noOfRemovedElements = 0
        self.limitOfRestructuring = limitOfRestructuring

    def __str__(self):
        """Defining str function to display/print heap."""

        string = "["
        for i in range(1, self.i , 1):
            string += str(self.heap[i]) + " "
        return string + "]"

    def extractMinimum(self):
        """Function to return the minimum element of the heap"""

        return self.heap[1]

    def getI(self):
        """Function to return the position where the next element can be added."""

        return self.i

    def insertElement(self, element , i ):
        """Function to insert an element in the heap.Input is element to be added and i is the value returned from getI() function"""

        self.heap[i] = element
        # Parent of ith position
        parenti = i // 2

        # Inserting element into the heap
        try:
            # Bubbling up
            if parenti != 0 and self.heap[i] < self.heap[parenti]:
                self.heap[i], self.heap[parenti] = self.heap[parenti], self.heap[i]
                self.insertElement(element, parenti)
            # Incrementing self.i position
            else:
                self.i += 1
                return

        except:
            # Bubbling up
            self.heap[i] = 'NaN'
            self.insertElement(element, parenti)
            return

    def removeMinimum(self, i = 1):
        """Function to remove the minimum element in the heap."""

        # Restructures heap to be a continuous list otherwise a lot of "Nan" noOfElements
        # due to removal of minimums a lot of times interfere with the logic of the program
        if self.noOfRemovedElements == self.limitOfRestructuring:
            self.restructureHeap()
            self.noOfRemovedElements  = 0

        # Base cases
        if self.heap[i] == 'NaN' :
            self.noOfRemovedElements += 1
            return
        if 2 * i + 1 > self.noOfElements or 2 * i > self.noOfElements:
            self.heap[i] == "NaN"
            self.noOfRemovedElements += 1
            return

        # Initializing children element positions
        child1 = 2 * i
        child2 = ( 2 * i ) + 1

        # Case when there are no children
        if self.heap[child1] == 'NaN' and self.heap[child2] == 'NaN':
            self.heap[i] = 'NaN'
            self.noOfRemovedElements += 1
            return

        # Case when there is only one child
        elif self.heap[child2] == 'NaN':
            self.heap[i], self.heap[child1] = self.heap[child1], "NaN"
            self.noOfRemovedElements += 1
            return

        # Case when there is only one child, same as above
        elif self.heap[child1] == 'NaN':
            self.heap[i], self.heap[child2] = self.heap[child2], "NaN"
            self.noOfRemovedElements += 1
            return

        # Swapping parent with the smaller child
        # Bubbling down
        if self.heap[child1] <= self.heap[child2]:
            self.heap[i], self.heap[child1] = self.heap[child1], self.heap[i]
            self.removeMinimum( child1 )
        else:
            self.heap[i], self.heap[child2] = self.heap[child2], self.heap[i]
            self.removeMinimum( child2 )

    def restructureHeap(self):
        """"Function to restructure heap to store elements in a continuous fashion in the list."""

        self.i = 1
        # Storing the elements that already exist in a temporary list
        tempList = []
        for heapElement in self.heap:
            if heapElement != "NaN" :
                tempList.append( heapElement )

        # Initializing new heap
        self.heap = ["NaN"] * self.noOfElements

        # Storing all the elements in the temporary list in a continuous fashion in the new heap
        for element in tempList:
            self.insertElement(element, self.i)

if __name__ == "__main__":
    main()
