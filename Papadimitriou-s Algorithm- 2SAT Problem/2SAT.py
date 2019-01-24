# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:49:45 2018

@author: Shashwat Kathuria
"""

# PAPADIMITRIOU'S ALGORITHM - 2-SAT PROBLEM

import random
import math
def main():

    # Reading inputs from the input file and storing clauses in a list
    file = open("2SAT1.txt", "r")
    noOfClauses = int( file.readline() )

    # List to store clauses
    clauses = []
    for i in range(noOfClauses):
        clauseLiteralsInfo = file.readline().split()
        clause = Clause( firstLiteral = int(clauseLiteralsInfo[0]), secondLiteral = int(clauseLiteralsInfo[1]))
        clauses.append(clause)

    # Calling papadimitriou's algorithm
    papadimitriou(clauses, noOfClauses)

def papadimitriou(clauses, noOfClauses):
    """Funtion to compute where or not a instance satisfies the 2-SAT property.
       Inputs are the clauses and number of clauses."""
    # List to store the values of the literals initialized above
    answers = []
    answers.append( "NaN" )
    for x in range(1, noOfClauses + 1):
        x = random.random()
        if x > 0.5:
            answers.append(True)
        else:
            answers.append(False)

    # Algorithm to run 2 * n^2 * logn times (loops)
    twoNSquared = 2 * (noOfClauses ** 2)

    # Flag to keep track if the input satisfies 2-SAT propety or not
    isSatisfying = False

    # Running for loop of algorithm
    for k in range( int( math.log(noOfClauses, 2) ) ):

        print("ON LOOP NUMBER :" + str(k))

        for j in range(twoNSquared):

            # Flag to keep track if all the clauses are satisfied or not
            # Helps in breaking early
            areAllClausesSatisfied = True

            # Variable to keep track of number of clauses satisfied till now
            # (of the clauses scanned)
            noOfSatisfyingClauses = 0

            # Running loop for every clause
            for clause in clauses:

                # If clause is not satisfying itself individually
                if clause.isSatisfyingCriteria(answers) == False:
                    areAllClausesSatisfied = False

                    # Randomly choosing a literal and negating its value
                    randomlyChosenLiteral = random.choices([clause.firstLiteral,clause.secondLiteral])[0]
                    answers[ abs(randomlyChosenLiteral) ] = not( answers[ abs(randomlyChosenLiteral) ] )

                    break

                # Else if the clause is satisfying itself individually
                else:
                    noOfSatisfyingClauses += 1

            print("The number of clauses satisfying criteria till now (of the ones which have been checked in a linear pass) is :" + str(noOfSatisfyingClauses) )

            # Breaking early if all the clauses are satisfied
            if areAllClausesSatisfied == True:
                isSatisfying = True
                break

        # Printing answers, values of the literals if 2-SAT property is satisfied by clauses
        if isSatisfying == True:
            # Printing results
            print("The answers of the literals respectively are as follows :- \n\n")
            for i in range(1, len(answers),1):
                print("Literal " + str(i) + " : " + str(answers[i]) )
            print("The instance is satisfiable")
            break

    # Printing not satisfiable if none of the iterations are able to find any solution
    if isSatisfying == False:
        print("The instance is not satisfiable")

class Clause:

    def __init__(self, firstLiteral, secondLiteral):
        """Function to initialize a new clause."""

        self.firstLiteral = firstLiteral
        self.secondLiteral = secondLiteral

    def __str__(self):
        """Function to print the clause in the required way."""

        return str(self.firstLiteral) + " OR " + str(self.secondLiteral)

    def isSatisfyingCriteria(self, answers):
        """Function to check whether the clause is satisfied or not."""

        # Negative value means negation
        # Positive value means no negation

        if self.firstLiteral < 0:
            boolean1 = not( answers[ abs(self.firstLiteral) ] )
        else:
            boolean1 = answers[ self.firstLiteral ]

        if self.secondLiteral < 0:
            boolean2 = not( answers[ abs(self.secondLiteral) ] )
        else:
            boolean2 = answers[ self.secondLiteral ]

        # Returning OR result of both the literals
        return boolean1 or boolean2

if __name__ == "__main__":
    main()
