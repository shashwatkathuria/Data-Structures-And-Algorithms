# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:32:47 2018

@author: Shashwat Kathuria
"""

# HEAP SORT

def main():

    # Reading elements from file and storing it inside a heap
    file = open("IntegerArray.txt", "r")
    noOfElements = int(file.readline())

    # Initializing heap
    minHeap = Heap(noOfElements = 5 * noOfElements , limitOfRestructuring = 30)

    # Storing elements in the heap
    for i in range(100000):
        element = int(file.readline())
        minHeap.insertElement(element = element, i = minHeap.getI())
    print("\nThe original heap looks as follows : \n\n" + str(minHeap))
    print("\n\n")

    # Calling heap sort algorithm on heap
    heapSort(minHeap)

def heapSort(minHeap):
    """Heap Sort Algorithm to sort a heap.Input is a minHeap."""

    #Initializing list to store sorted elements
    arr = []
    print("\n")

    # Looping to get the minimum element in each iteration and then removing it from the heap
    for i in range(minHeap.getI()):
        print("ON ITERATION NO : " + str( i) + " OUT OF " + str(100000))
        arr.append(minHeap.extractMinimum())
        minHeap.removeMinimum()

    print("\n\nThe sorted array looks as follows : \n\n")
    print(arr)
    print("\n")


class Heap:

    def __init__(self, noOfElements, limitOfRestructuring):
        """"Initializes heap instance.Inputs are no of elements in heap and limit of restructuring of heap."""

        self.heap = [ 'NaN' ] * (noOfElements + 1)
        self.noOfElements = noOfElements + 1
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
