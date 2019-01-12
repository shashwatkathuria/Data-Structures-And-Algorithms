#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include<fstream>
#include "persondllclasshelpers.h"
using namespace std;

int main(void)
{
    PersonDoublyLinkedList dll_1;
    Person p;
    char fname[15];
    char lname[15];
    int age;
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
        dll_1.insertNode(p);

    }
    fin.close();
    int choice = 0;
    cout<<endl<<"THE INPUT.TXT IS SUCCESSFULLY INSERTED INTO THE LINKED LIST";
    cout<<endl<<"PLEASE CHOOSE AMONG THE FOLLOWING OPERATIONS TO DO AS YOU LIKE";
    do
    {
        cout<<endl<<"______________________________";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"-||PLEASE REMEMBER TO SCROLL ABOVE TO SEE THE OUTPUTS||-";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"DOUBLY LINKED LIST";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"1. Insert an element into the doubly linked list";
        cout<<endl<<"2. Delete an element from the doubly linked list";
        cout<<endl<<"3. Traverse the doubly linked list";
        cout<<endl<<"4. Search for an element";
        cout<<endl<<"5. Sort the list";
        cout<<endl<<"6. Get the number of elements in the list";
        cout<<endl<<"7. Delete whole doubly linked list";
        cout<<endl<<"0. QUIT";
        cout<<endl<<endl<<"Enter your choice:  ";
        cin>>choice;
        cout<<endl<<"______________________________";
        switch (choice)
        {
            case 1:
                cout<<endl<<"Enter the element you want to insert: ";
                cout<<endl<<"Enter FIRST name of person:  ";
                cin>>fname;
                cout<<endl<<"Enter LAST name of person:  ";
                cin>>lname;
                cout<<endl<<"Enter the AGE of the person:  ";
                cin>>age;
                p.setName(fname, lname);
                p.setAge(age);
                cout<<endl<<"_________________________________"<<endl;
                dll_1.insertNode(p);
                break;

            case 2:
                cout<<"Enter the element to delete :  ";
                cout<<endl<<"Enter FIRST name of person:  ";
                cin>>fname;
                cout<<endl<<"Enter LAST name of person:  ";
                cin>>lname;
                cout<<endl<<"Enter the AGE of the person:  ";
                cin>>age;
                p.setName(fname, lname);
                p.setAge(age);
                cout<<endl<<"_________________________________"<<endl;
                dll_1.deleteNode(p);
                break;

            case 3:
                cout<<endl<<"_________________________________"<<endl;
                dll_1.traverseList();
                break;

            case 4:
                cout<<endl<<"Enter the element you want to search for:  ";
                cout<<endl<<"Enter FIRST name of person:  ";
                cin>>fname;
                cout<<endl<<"Enter LAST name of person:  ";
                cin>>lname;
                cout<<endl<<"Enter the AGE of the person:  ";
                cin>>age;
                p.setName(fname, lname);
                p.setAge(age);
                cout<<endl<<"_________________________________"<<endl;
                dll_1.searchNode(p);
                break;
            case 5:
                cout<<endl<<"_________________________________"<<endl;
                dll_1.sort();
                break;
            case 6:
                cout<<endl<<"The number of elements in the list are: "<<dll_1.length;
                break;
            case 7:
                dll_1.deleteWholeDLL();
                break;
            case 0:
                cout<<endl<<"BYE!!!";
                break;
            default:
                cout<<endl<<"INVALID CHOICE!!!!";
                break;
        }
    }
    while (choice != 0);

}

