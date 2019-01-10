# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 19:16:09 2018

@author: Shashwat Kathuria
"""

class Job:

    def __init__(self, weight, length):
        self.weight = weight
        self.length = length
        self.weightToLengthRatio = float(weight) / float(length)

    def __str__(self):
        return "Weight : " + str(self.weight) + " Length : " + str(self.length) + " Ratio : " + str( self.weightToLengthRatio )

def main():

    file = open("JOBS.txt", "r")
    noOfJobs = int(file.readline())
    jobs = []
    for i in range(noOfJobs):
        jobInfo = file.readline().split(" ")
        job = Job( weight = int( jobInfo[0] ), length = int( jobInfo[1] ) )
        jobs.append(job)

    # for job in jobs:
    #     print(job)

    # Algorithm 1 - Job weight - Job length
    jobs.sort( reverse = True, key = lambda x : x.weight )
    jobs.sort( reverse = True, key = lambda x : x.weight - x.length )

    time = 0
    wrongCompletionWeight = 0
    for job in jobs:
        time += job.length
        wrongCompletionWeight += time * job.weight

    print("The answer obtained from the WRONG job scheduling greedy algorithm (Weight - Length) is : " + str(wrongCompletionWeight))


    # Algorithm 2 - Job weight/ Job length
    jobs.sort( reverse = True, key = lambda x : x.weightToLengthRatio )

    time = 0
    correctCompletionWeight = 0
    for job in jobs:
        time += job.length
        correctCompletionWeight += time * job.weight

    print("The answer obtained from the CORRECT job scheduling greedy algorithm (Weight / Length) is : " + str(correctCompletionWeight))

if __name__ == "__main__":
    main()
