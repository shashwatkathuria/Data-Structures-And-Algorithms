# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:16:09 2019
@author: Shashwat Kathuria
"""

from PIL import Image

image = Image.open("i3.png")
image = image.convert("RGB")
width, height = image.size
imagePixels = []
disjointSets = []


def main():

    for i in range(width):
        for j in range(height):
            r, g, b = image.getpixel((i, j))
            tempPixel = ImagePixel(i, j, r, g, b)
            imagePixels.append(tempPixel)
            if tempPixel.isBlack:
                disjointSets.append([tempPixel])

    temp = len(disjointSets)
    print(len(disjointSets))

    for i in range(len(imagePixels)):

            pixel = imagePixels[i]
            print("Reducing...Please Wait..." + str(len(disjointSets)))
            if pixel.isRightPixelNeighbour(image):
                u = findClusterIndex(pixel.x + 1, pixel.y)
                v = findClusterIndex(pixel.x, pixel.y)
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])
            if pixel.isLeftPixelNeighbour(image):
                u = findClusterIndex(pixel.x - 1, pixel.y)
                v = findClusterIndex(pixel.x, pixel.y)
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])
            if pixel.isUpperPixelNeighbour(image):
                u = findClusterIndex(pixel.x, pixel.y - 1)
                v = findClusterIndex(pixel.x, pixel.y)
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])
            if pixel.isBottomPixelNeighbour(image):
                u = findClusterIndex(pixel.x, pixel.y + 1)
                v = findClusterIndex(pixel.x, pixel.y)
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])



    print("The total number of digits in this image is : " + str(len(disjointSets)))


class ImagePixel:

    def __init__(self, x, y, r, g, b):
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.isBlack = (self.r == 0 and self.g == 0 and self.b == 0)
        self.set = -1

    def isLeftPixelNeighbour(self, image):
        if self.x != 0:
            r, g, b = image.getpixel((self.x - 1, self.y))
            isBlack = r == 0 and g == 0 and b == 0
            if self.r == r and self.g == g and self.b == b and isBlack:
                return True
            else:
                return False
        else:
            return False

    def isUpperPixelNeighbour(self, image):
        if self.y != 0:
            r, g, b = image.getpixel((self.x, self.y - 1))
            isBlack = r == 0 and g == 0 and b == 0
            if self.r == r and self.g == g and self.b == b and isBlack:
                return True
            else:
                return False
        else:
            return False

    def isRightPixelNeighbour(self, image):
        if self.x != width - 1:
            r, g, b = image.getpixel((self.x + 1, self.y))
            isBlack = r == 0 and g == 0 and b == 0
            if self.r == r and self.g == g and self.b == b and isBlack:
                return True
            else:
                return False
        else:
            return False

    def isBottomPixelNeighbour(self, image):
        if self.y != height - 1:
            r, g, b = image.getpixel((self.x, self.y + 1))
            isBlack = r == 0 and g == 0 and b == 0
            if self.r == r and self.g == g and self.b == b and isBlack:
                return True
            else:
                return False
        else:
            return False

    def find(self, array, x, y):
        for i in range(len(array)):
            pixel = array[i]
            if pixel.x == x and pixel.y == y:
                return pixel

    def __str__(self):
        return ("X : " + str(self.x) + " Y : " + str(self.y) + " R : " + str(self.r) + " G : " + str(self.g) + " B : " + str(self.b))

def mergeClusters(cluster1, cluster2):

    listi = cluster1
    listj = cluster2

    ltemp = listi[:] + listj[:]
    disjointSets.remove(listi)
    disjointSets.remove(listj)
    disjointSets.append(ltemp)

def findClusterIndex(x, y):
    for i in range( len(disjointSets) ):
        for element in disjointSets[i]:
            if element.x == x and element.y == y and element.isBlack:
                return i



if __name__ == "__main__":
    main()
