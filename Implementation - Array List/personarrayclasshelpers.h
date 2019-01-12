#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include "personclasshelpers.h"
using namespace std;


class PersonArray
{
    public:

        int length;
        Person arr[100];
        void insertElementAtIndex(int index, Person element);
        void deleteElementAtIndex(int index);
        void display();
        void sort();
        void searchForElement(Person p);
        PersonArray()
        {
            length=0;
        }

};

void PersonArray::insertElementAtIndex(int index,Person element)
{
    if (length < 100 && (index - 1) <= length)
    {
        for (int i = 99; i > index - 1; i--)
        {
            arr[i] = arr[i - 1];
        }
        arr[index - 1] = element;
        length++;
    }
    else if (index > length && length < 100)
    {
        cout<<"INVALID INDEX!!"<<"ADD THE PERSON TO A POSITION LESS THAN OR EQUAL TO "<<length + 1;
    }
    else if (length == 100)
    {
        cout<<"ARRAY OUT OF SPACE!!MAKE SOME SPACE TO ENTER MORE PERSONS!!";
    }

}

void PersonArray::deleteElementAtIndex(int index)
{
    if ((index - 1) < length)
    {
        Person deleted = arr[index - 1];

        for(int i = index - 1; i < 99; i++)
        {
            arr[i] = arr[i + 1];
        }
        cout<<"\n The element deleted is: ";
        deleted.display();
        cout<<endl;
        --length;
    }
    else
    {
        cout<<"INVALID INDEX!!!";
        cout<<endl;
    }

}
void PersonArray::display()
{
    int size = length;
    for (int i = 0; i < size; i++)
    {
        cout<<endl<<"The "<<i + 1<<" th person is ";
        arr[i].display();
        cout<<endl;
    }

}

void PersonArray::sort()
{
    for (int i = 0; i < length; i++)
    {
        for (int j = i + 1; j < length; j++)
        {
            if (arr[i] > arr[j])
            {
                Person temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
    }
    cout<<"DONE!!!ARRAY IS SORTED!!";
    cout<<endl;
}


void PersonArray::searchForElement(Person p)
{
    int flag = 1;
    for(int i = 0;i < length; i++)
    {
        if ((strcmpi(arr[i].firstname, p.firstname) == 0) && (strcmpi(arr[i].lastname, p.lastname) == 0) && (arr[i].getAge() == p.getAge()))
        {
            flag = 0;
            cout<<"FOUND THE ELEMENT AT "<<i + 1<<"th POSITION"<<endl;
            arr[i].display();
            cout<<endl;
        }
    }
    if (flag == 1)
    {
        cout<<"ELEMENT NOT IN LIST";
    }

}
