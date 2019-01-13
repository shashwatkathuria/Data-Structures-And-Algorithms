# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 14:32:47 2018

@author: Shashwat Kathuria
"""
def main():

    file = open("IntegerArray.txt", "r")
    noOfElements = int(file.readline())

    minHeap = Heap(noOfElements = 5 * noOfElements , limitOfRestructuring = 30)

    for i in range(100000):
        element = int(file.readline())
        minHeap.insertElement(element = element, i = minHeap.getI())
    print("\nThe original heap looks as follows : \n\n" + str(minHeap))
    print("\n\n")

    heapSort(minHeap)

def heapSort(minHeap):
    arr = []
    print("\n")
    for i in range(minHeap.getI()):
        print("ON ITERATION NO : " + str( i) + " OUT OF " + str(100000))
        arr.append(minHeap.extractMinimum())
        minHeap.removeMinimum()
    print("\n\nThe sorted array looks as follows : \n\n")
    print(arr)
    print("\n")


class Heap:

    def __init__(self, noOfElements, limitOfRestructuring):
        self.heap = [ 'NaN' ] * (noOfElements + 1)
        self.noOfElements = noOfElements + 1
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
