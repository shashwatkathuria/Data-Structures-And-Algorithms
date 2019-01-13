#include<iostream>
#include<fstream>
#include"personclasshelpers.h"
#include"bsthelpers.h"
using namespace std;


int main(void)
{
    BinarySearchTree bst_1;
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
    cout<<endl<<"DISPLAYING BST AFTER EACH INSERT AS REQUIRED:";
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
        bst_1.insert(bst_1.root,p);

    }

    fin.close();
    int choice = 0;
    cout<<endl<<"THE INPUT.TXT IS SUCCESSFULLY INSERTED INTO THE BINARY SEARCH TREE";
    cout<<endl<<"PLEASE CHOOSE AMONG THE FOLLOWING OPERATIONS TO DO AS YOU LIKE";
    cout<<endl<<"_________________________________";
    do
    {
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"-||PLEASE REMEMBER TO SCROLL ABOVE TO SEE THE OUTPUTS||-";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"BINARY SEARCH TREE ";
        cout<<endl<<"--------------------------------------------------------";
        cout<<endl<<"1. Insert a person into BST ";
        cout<<endl<<"2. Delete a person from BST ";
        cout<<endl<<"3. Search for a person in BST ";
        cout<<endl<<"4. Print the BST in order";
        cout<<endl<<"5. Get the number of persons in the BST";
        cout<<endl<<"0. Exit";
        cout<<endl<<"Enter a choice:  ";
        cin>>choice;
        cout<<endl<<"_________________________________"<<endl;

        switch (choice)
        {
            case 1:
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
                bst_1.insert(bst_1.root, p);
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
                bst_1.deleteNode(bst_1.root,p);
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
                bst_1.search(bst_1.root,p);
                break;
            case 4:
                bst_1.traversal(bst_1.root);
                break;
            case 5:
                cout<<endl<<"The number of persons stored in the list are: "<<bst_1.noofelements;
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

