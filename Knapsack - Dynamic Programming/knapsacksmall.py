# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:59:15 2018

@author: Shashwat Kathuria
"""
def main():
    try:
        file = open("SmallKnapsack.txt","r")
    except:
        print("Could not open the file.Error")
        return
    knapsackInfo = file.readline().split(" ")
    capacity = int(knapsackInfo[0])
    noofitems = int(knapsackInfo[1])

    items = {}
    for i in range(noofitems):
        tempItemInfo = file.readline().split(" ")
        items[i + 1] = [ int(tempItemInfo[0]), int(tempItemInfo[1]) ]

    answer = SmallKnapsack(noofitems, capacity, items)
    print("The optimal Knapsack solution is : " + str( answer[noofitems, capacity] ))

def SmallKnapsack(noofitems, capacity, items):
    ans = {}
    for x in range(capacity + 1):
        ans[0, x] = 0

    for i in range(1, noofitems + 1):
         print(i)
         for x in range(capacity + 1):
             if items[i][1] > x:
                 ans[i, x] = ans[i - 1, x]
                 continue
             a1 = ans[i - 1, x]
             a2 = ans[i - 1, x - items[i][1]] + items[i][0]
             if a2 > a1:
                 ans[i, x] = a2
             else:
                 ans[i, x] = a1
    return ans


if __name__ == "__main__":
    main()
