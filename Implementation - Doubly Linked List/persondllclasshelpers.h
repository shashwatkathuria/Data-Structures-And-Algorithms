#include<iostream>
#include<string.h>
#include<stdlib.h>
#include<ctype.h>
#include "personclasshelpers.h"
using namespace std;

struct node
{
  Person person;
  struct node *next;
  struct node *previous;
};

class PersonDoublyLinkedList
{
    public:

    node *root;
    int length;
    PersonDoublyLinkedList()
    {
        root = NULL;
        length = 0;
    }

    void insertNode(Person p);
    void traverseList();
    void searchNode(Person p);
    void deleteNode(Person p);
    void sort();
    void deleteWholeDLL();
};

void PersonDoublyLinkedList::sort()
{
    if (root != NULL)
    {
        cout<<endl<<"BEFORE SORTING,THE LIST LOOKED LIKE.."<<endl;
        traverseList();
        int counter;
        for (int i = 0; i < length; i++)
        {
            counter = 0;
            node *k1 = root;
            node *k2 = root->next;
            while (k2 != NULL)
            {
                if ( (k1->person).getAge() > (k2->person).getAge() )
                {
                    Person temp = k1->person;
                    k1->person = k2->person;
                    k2->person = temp;
                    counter++;

                }
                k1 = k1->next;
                k2 = k2->next;
            }
            if (counter == 0)
            {
                cout<<endl<<"AFTER SORTING THE LIST LOOKS LIKE..."<<endl;
                traverseList();
                return;
            }
        }
        cout<<endl<<"AFTER SORTING THE LIST LOOKS LIKE..."<<endl;
        traverseList();
    }
    else
    {
        cout<<endl<<"YOU NEED TO INSERT SOME ELEMENTS INTO THE LIST IN ORDER TO SORT IT!!"<<endl;
    }
}

void PersonDoublyLinkedList::searchNode(Person p)
{
    if(root != NULL)
    {
        int i = 1;
        node *temp = root;
        while (temp != NULL)
        {
            if ( (strcmpi( (temp->person).firstname, p.firstname) == 0) && (strcmpi( (temp->person).lastname, p.lastname) == 0)&& ( (temp->person).getAge() == p.getAge() ) )
            {
                cout<<"\nFOUND THE ELEMENT AT POSITION "<<i<<endl;
                (temp->person).display();
                cout<<endl;
                return;
            }
            else
            {
                temp = temp->next;
                i++;
            }

        }
        cout<<endl<<"COULD NOT FIND THE ELEMENT ";
        p.display();
        cout<<endl;
    }
    else
    {
        cout<<"THERE ARE NO ELEMENTS IN THE LIST!!";
    }

}

void PersonDoublyLinkedList::deleteNode(Person p)
{
    if (root != NULL)
    {
        node *temp = root;
        while (temp != NULL )
        {
            if ( (strcmpi( (temp->person).firstname, p.firstname) == 0) && (strcmpi( (temp->person).lastname, p.lastname) == 0) && ( (temp->person).getAge() == p.getAge() ) )
            {
                --length;
                cout<<"\nDELETING THE ELEMENT ";
                p.display();
                cout<<endl;
                node *current = temp;
                node *forward = temp->next;
                if ( (current->previous) != NULL && forward != NULL)
                {
                    temp = temp->previous;
                    temp->next = forward;
                    forward->previous = temp;
                    current->previous = NULL;
                    current->next = NULL;
                    current = NULL;
                    forward = NULL;
                    return;
                }
                else if ( current->previous == NULL && forward != NULL)
                {
                    forward->previous = NULL;
                    root = forward;
                    current->next = NULL;
                    current = NULL;
                    forward = NULL;
                    return;
                }
                else if ( current->previous != NULL && forward == NULL )
                {
                    temp = temp->previous;
                    temp->next = NULL;
                    current->previous = NULL;
                    current = NULL;
                    return;
                }
                else if (current->previous == NULL && forward == NULL)
                {
                    root = NULL;
                    forward = NULL;
                }
                if (length == 0)
                {
                    return;
                }

            }
            else
            {
                temp = temp->next;
            }

        }
        cout<<endl<<"COULD NOT FIND THE ELEMENT "<<endl;
        p.display();
        cout<<endl;
    }
    else
    {
        cout<<"THERE ARE NO ELEMENTS IN THE LIST!! ";
    }
}

void PersonDoublyLinkedList::insertNode(Person p)
{
    if (root != NULL)
    {
        node *temp = new node;
        temp->person = p;
        temp->next = root;
        root->previous = temp;
        temp->previous = NULL;
        root = temp;
        temp = NULL;
    }
    else
    {
        node* temp = new node;
        temp->person = p;
        temp->next = NULL;
        temp->previous = NULL;
        root = temp;
        temp = NULL;

    }
    length++;
}

void PersonDoublyLinkedList::traverseList()
{
    if (root != NULL)
    {
        int i = 1;
        node *k = root;
        cout<<endl;
        while (k != NULL)
        {
            cout << i << "th element is ";
            (k->person).display();
            cout<< endl;
            if (k->next != NULL)
            {
                k = k->next;
            }
            else
            {
                break;
            }
            i++;
        }

    }
    else
    {
        cout<<"THERE ARE NO ELEMENTS IN THE LIST!!";
    }
}

void PersonDoublyLinkedList::deleteWholeDLL()
{
    if (root != NULL)
    {
        node *k = root;
        while (k != NULL)
        {
            node *temp = k->next;
            k->next = NULL;
            k->previous = NULL;
            k = temp;
        }
        root = NULL;
        cout<<"DELETED WHOLE LIST!!";
        length = 0;
    }
    else
    {
        cout<<endl<<"LIST IS ALREADY EMPTY!!";
    }
}
