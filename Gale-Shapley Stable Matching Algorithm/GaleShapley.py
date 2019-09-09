# -*- coding: utf-8 -*-
"""
Created on Sat Sep 7 0:21:55 2019

@author: Shashwat Kathuria
"""

matchings = {}
companies = {}
students = {}

def main():
    companyFile = open("m.txt")
    studentFile = open("w.txt")

    for line in companyFile.readlines():
        companyInfo = line[:-1].split(" ")
        companies[companyInfo[0]] = [companyInfo[1:], True]
        # companies.append(company)

    for line in studentFile.readlines():
        studentInfo = line[:-1].split(" ")
        students[studentInfo[0]] = studentInfo[1:]

    print(students)
    print(companies)
    for student in students:
        matchings[student] = ""

    freeCompanies = len(companies)

    while freeCompanies != 0:
        for company in companies:
            companyName = company
            companyPreferenceList = companies[company][0]
            for student in companyPreferenceList:
                print()
                print(companyName, "-", student)

                if companies[companyName][1] == True:

                    if matchings[student] == "":
                        print(student + " accepts " + companyName)
                        matchings[student] = companyName
                        companies[companyName][1] = False
                        freeCompanies -= 1

                    elif students[student].index(companyName) < students[student].index(matchings[student]):
                        print(student + " dumps " + matchings[student] + " and accepts " + companyName + ".")

                        companies[companyName][1] = False
                        companies[matchings[student]][1] = True
                        matchings[student] = companyName

                    else:
                        print(student + " rejects " + companyName)
                else:
                    print(companyName + " not free.")
            print("\n\n")
    print("----------\nANSWER\n----------")
    print(matchings)


if __name__ == "__main__":
    main()
