# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 15:16:09 2019
@author: Shashwat Kathuria
"""

# DISJOINT SET - NUMBER OF DIGITS IN IMAGE RECOGNITION ALGORITHM

# Importing required library class
from PIL import Image

# Initializing required variables
image = Image.open("image2.png")
# Converting Image to RGB
image = image.convert("RGB")
width, height = image.size
imagePixels = []
disjointSets = []

def main():

    # Scanning through all the pixels in the image
    for i in range(width):
        for j in range(height):
            # Getting r, g, b values of image at i, j location
            r, g, b = image.getpixel((i, j))
            # Storing pixel
            tempPixel = ImagePixel(i, j, r, g, b)
            # Appending image pixel object to image pixel list
            imagePixels.append(tempPixel)
            # Adding image to disjoint sets only if black
            # Because black and white images are being analyzed
            # With digits being black
            if tempPixel.isBlack:
                disjointSets.append([tempPixel])

    # Scanning through all image pixels
    for i in range(len(imagePixels)):

            # Checking for neighbours of current pixel and merging its
            # disjoint set to neighbouring disjoint set if condition holds true
            pixel = imagePixels[i]
            print("Reducing...Please Wait..." + str(len(disjointSets)))
            # Right pixel
            if pixel.isRightPixelNeighbour(image):
                u = findClusterIndex(pixel.x + 1, pixel.y)
                v = findClusterIndex(pixel.x, pixel.y)
                # Merging if not already in same cluster
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])
            # Left Pixel
            if pixel.isLeftPixelNeighbour(image):
                u = findClusterIndex(pixel.x - 1, pixel.y)
                v = findClusterIndex(pixel.x, pixel.y)
                # Merging if not already in same cluster
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])
            # Upper Pixel
            if pixel.isUpperPixelNeighbour(image):
                u = findClusterIndex(pixel.x, pixel.y - 1)
                v = findClusterIndex(pixel.x, pixel.y)
                # Merging if not already in same cluster
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])
            # Bottom Pixel
            if pixel.isBottomPixelNeighbour(image):
                u = findClusterIndex(pixel.x, pixel.y + 1)
                v = findClusterIndex(pixel.x, pixel.y)
                # Merging if not already in same cluster
                if u != v:
                    mergeClusters(disjointSets[u], disjointSets[v])


    # Printing answer
    print("The total number of digits in this image is : " + str(len(disjointSets)))

# Class for image pixel
class ImagePixel:

    def __init__(self, x, y, r, g, b):
        """Function to initialize image pixel."""
        self.x = x
        self.y = y
        self.r = r
        self.g = g
        self.b = b
        self.isBlack = (self.r == 0 and self.g == 0 and self.b == 0)
        self.set = -1

    def isLeftPixelNeighbour(self, image):
        """Function to check if left image pixel is a neighbour, i.e.,
        if it is same in colour(black)."""
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
        """Function to check if upper image pixel is a neighbour, i.e.,
        if it is same in colour(black)."""
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
        """Function to check if right image pixel is a neighbour, i.e.,
        if it is same in colour(black)."""
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
        """Function to check if bottom image pixel is a neighbour, i.e.,
        if it is same in colour(black)."""
        if self.y != height - 1:
            r, g, b = image.getpixel((self.x, self.y + 1))
            isBlack = r == 0 and g == 0 and b == 0
            if self.r == r and self.g == g and self.b == b and isBlack:
                return True
            else:
                return False
        else:
            return False

    def __str__(self):
        """Function to print image pixel."""
        return ("X : " + str(self.x) + " Y : " + str(self.y) + " R : " + str(self.r) + " G : " + str(self.g) + " B : " + str(self.b))

def mergeClusters(cluster1, cluster2):
    """Function to merge two clusters."""
    listi = cluster1
    listj = cluster2

    # Merging and copying to avoid aliasing effect
    ltemp = listi[:] + listj[:]

    # Removing clusters
    disjointSets.remove(listi)
    disjointSets.remove(listj)
    # Adding merged cluster
    disjointSets.append(ltemp)

def findClusterIndex(x, y):
    """Function to find cluster index."""

    for i in range( len(disjointSets) ):
        for element in disjointSets[i]:
            if element.x == x and element.y == y and element.isBlack:
                return i

# Calling main function
if __name__ == "__main__":
    main()
