#include<iostream>
#include<stdio.h>
#include<fstream>
#include "personclasshelpers.h"
#include "stackhelpers.h"
using namespace std;

int main(void)
{
    Stack stk_1;
    char fname[15];
    char lname[15];
    int age;
    Person p;
    int n;
    ifstream fin;
    fin.open("input.txt");
    if(!fin.is_open())
    {
        cout<<"COULD NOT OPEN THE FILE";
        return 0;
    }
    char noofelements[15];
    fin>>noofelements;
    n=atoi(noofelements);
    for (int i=0; i<n; i++)
    {
        char firstname[15];
        char lastname[15];
        fin>>firstname;
        fin>>lastname;
        char age_[15];
        fin>>age_;
        age=atoi(age_);
        p.setName(firstname, lastname);
        p.setAge(age);
        stk_1.push(p);

    }
    fin.close();
    int choice = 0;
    cout<<endl<<"THE INPUT.TXT IS SUCCESSFULLY INSERTED INTO THE STACK";
    cout<<endl<<"PLEASE CHOOSE AMONG THE FOLLOWING OPERATIONS TO DO AS YOU LIKE";
    cout<<endl<<"_________________________________";
    do
    {
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"-||PLEASE REMEMBER TO SCROLL ABOVE TO SEE THE OUTPUTS||-";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"STACK ";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"1. Push (Insert) an element into Stack ";
        cout<<endl<<"2. Pop (Delete) top element from Stack ";
        cout<<endl<<"3. Search for a person in Stack ";
        cout<<endl<<"4. Print the Stack from top to bottom";
        cout<<endl<<"5. Get the number of persons in the Stack";
        cout<<endl<<"6. Delete the whole Stack";
        cout<<endl<<"0. Exit";
        cout<<endl<<"Enter a choice:  ";
        cin>>choice;
        cout<<endl<<"_________________________________"<<endl;

        switch (choice)
        {
            case 1:
                cout<<"Enter the element to push :  ";
                cout<<endl;
                cout<<endl<<"Enter FIRST NAME of person:  ";
                cin>>fname;
                cout<<endl<<"Enter LAST NAME of person:  ";
                cin>>lname;
                cout<<endl<<"Enter the AGE of the person:  ";
                cin>>age;
                p.setName(fname, lname);
                p.setAge(age);
                cout<<endl<<"_________________________________"<<endl;
                stk_1.push(p);
                break;

            case 2:
                stk_1.pop();
                break;
            case 3:
                cout<<endl<<"Enter element to search for:  ";
                cout<<endl<<"Enter FIRST NAME of person:  ";
                cin>>fname;
                cout<<endl<<"Enter LAST NAME of person:  ";
                cin>>lname;
                cout<<endl<<"Enter the AGE of the person:  ";
                cin>>age;
                p.setName(fname, lname);
                p.setAge(age);
                cout<<endl<<"_________________________________"<<endl;
                stk_1.search(p);
                break;
            case 4:
                stk_1.displayStack();
                break;
            case 5:
                cout<<endl<<"The number of persons stored in the list are: "<<stk_1.size;
                break;
            case 6:
                stk_1.deleteStack();
                break;
            case 0:
                cout<<"BYE!!!";
                break;

            default:
                cout<<endl<<"YOU ENTERED AN INVALID CHOICE!!!";
                break;

        }
    cout<<endl<<"_________________________________";
    }
    while (choice != 0);
    cout<<endl;
}