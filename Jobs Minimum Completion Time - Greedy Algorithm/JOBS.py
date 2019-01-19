# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 19:16:09 2018

@author: Shashwat Kathuria
"""

# JOBS MINIMUM TIME COMPLETION ALGORITHM - GREEDY ALGORITHM

def main():

    # Reading inputs from the file and storing the jobs
    file = open("JOBS.txt", "r")
    noOfJobs = int(file.readline())

    # List to store jobs
    jobs = []
    for i in range(noOfJobs):
        jobInfo = file.readline().split(" ")
        job = Job( weight = int( jobInfo[0] ), length = int( jobInfo[1] ) )
        jobs.append(job)

    # Printing input jobs
    print("\nThe input jobs are: \n\n")

    for job in jobs:
        print(job)

    print("\n\n")

    # Algorithm 1 - Job weight - Job length -> In ascending order
    # For solving collisions, refering to job with more weight
    # WRONG ALGORITHM
    jobs.sort( reverse = True, key = lambda x : x.weight )
    jobs.sort( reverse = True, key = lambda x : x.weight - x.length )

    time = 0
    wrongCompletionWeight = 0
    for job in jobs:
        time += job.length
        wrongCompletionWeight += time * job.weight

    print("The answer obtained from the WRONG job scheduling greedy algorithm (Weight - Length) is : " + str(wrongCompletionWeight))


    # Algorithm 2 - Job weight/ Job length -> In ascending order
    # CORRECT ALGORITHM
    jobs.sort( reverse = True, key = lambda x : x.weightToLengthRatio )

    time = 0
    correctCompletionWeight = 0
    for job in jobs:
        time += job.length
        correctCompletionWeight += time * job.weight

    print("The answer obtained from the CORRECT job scheduling greedy algorithm (Weight / Length) is : " + str(correctCompletionWeight))


class Job:

    def __init__(self, weight, length):
        """Function to initialize the job."""
        self.weight = weight
        self.length = length
        self.weightToLengthRatio = float(weight) / float(length)

    def __str__(self):
        """Function to print the job in the required way."""

        return "Weight : " + str(self.weight) + " Length : " + str(self.length) + " Ratio : " + str( self.weightToLengthRatio )

if __name__ == "__main__":
    main()
