#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<fstream>
#include "personarrayclasshelpers.h"
using namespace std;

int main(void)
{
    PersonArray arr_1;
    int index;
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
        arr_1.insertElementAtIndex(i+1,p);

    }

    fin.close();
    int choice = 0;
    cout<<endl<<"THE INPUT.TXT IS SUCCESSFULLY INSERTED INTO THE ARRAY";
    cout<<endl<<"PLEASE CHOOSE AMONG THE FOLLOWING OPERATIONS TO DO AS YOU LIKE";
    cout<<endl<<"_________________________________";
    do
    {
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"-||PLEASE REMEMBER TO SCROLL ABOVE TO SEE THE OUTPUTS||-";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"PERSON ARRAY ";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"1. Insert a person into array ";
        cout<<endl<<"2. Delete a person from array ";
        cout<<endl<<"3. Search for a person in array ";
        cout<<endl<<"4. Display the array ";
        cout<<endl<<"5. Sort the array";
        cout<<endl<<"6. Get the number of persons in the person array";
        cout<<endl<<"0. Exit";
        cout<<endl<<"Enter a choice:  ";
        cin>>choice;
        cout<<endl<<"_________________________________"<<endl;

        switch (choice)
        {
            case 1:
                cout<<"Enter the POSITION in which to insert element :  ";
                cin>>index;
                cout<<"Enter the element to insert :  ";
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
                arr_1.insertElementAtIndex(index, p);
                break;

            case 2:
                cout<<"Enter the POSITION from which to delete the element :  ";
                cin>>index;
                cout<<endl<<"_________________________________"<<endl;
                arr_1.deleteElementAtIndex(index);
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
                arr_1.searchForElement(p);
                break;
            case 4:
                arr_1.display();
                break;
            case 5:
                arr_1.sort();
                arr_1.display();
                break;
            case 6:
                cout<<endl<<"The number of persons stored in the list are: "<<arr_1.length;
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