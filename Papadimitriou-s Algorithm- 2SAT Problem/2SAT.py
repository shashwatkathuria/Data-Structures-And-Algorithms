# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 16:49:45 2018

@author: Shashwat Kathuria
"""
import random
import math
isSatisfying = False
class Clause:

    def __init__(self, firstLiteral, secondLiteral):

        self.firstLiteral = firstLiteral
        self.secondLiteral = secondLiteral

    def __str__(self):
        return str(self.firstLiteral) + " OR " + str(self.secondLiteral)

    def isSatisfyingCriteria(self):

           if self.firstLiteral < 0:
               boolean1 = not( answers[ abs(self.firstLiteral) ] )
           else:
               boolean1 = answers[ self.firstLiteral ]

           if self.secondLiteral < 0:
               boolean2 = not( answers[ abs(self.secondLiteral) ] )
           else:
               boolean2 = answers[ self.secondLiteral ]

           return boolean1 or boolean2


file = open("2SAT1.txt", "r")
noOfClauses = int( file.readline() )

clauses = []
for i in range(noOfClauses):
    clauseLiteralsInfo = file.readline().split()
    clause = Clause( firstLiteral = int(clauseLiteralsInfo[0]), secondLiteral = int(clauseLiteralsInfo[1]))
    clauses.append(clause)



answers = []
answers.append( "NaN" )
for x in range(1, noOfClauses + 1):
    x = random.random()
    if x > 0.5:
        answers.append(True)
    else:
        answers.append(False)



twoNSquared = 2 * (noOfClauses ** 2)
for k in range( int( math.log(noOfClauses, 2) ) ):

    print(k)

    for j in range(twoNSquared):

        flag = True
        noOfSatisfyingClauses = 0
        for clause in clauses:
            randomlyChosenLiteral = random.choices([clause.firstLiteral,clause.secondLiteral])[0]
            if clause.isSatisfyingCriteria() == False:
                flag = False
                answers[ abs(randomlyChosenLiteral) ] = not( answers[ abs(randomlyChosenLiteral) ] )
                break
            else:
                noOfSatisfyingClauses += 1

        print("The number of clauses satisfying criteria till now (of the ones which have been checked) is :" + str(noOfSatisfyingClauses) )

        if flag == True:
            isSatisfying = True
            break

    if isSatisfying == True:
        print("The answers of the literals respectively are as follows :- \n\n")
        for i in range(1, len(answers),1):
            print("Literal " + str(i) + " : " + str(answers[i]) )
        print("The instance is satisfiable")
        break

if isSatisfying == False:
    print("The instance is not satisfiable")
