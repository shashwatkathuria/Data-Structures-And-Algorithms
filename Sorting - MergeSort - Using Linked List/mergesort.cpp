#include<iostream>
#include<fstream>
#include<stdlib.h>

using namespace std;

struct node
{
    long int x;
    struct node *next;
};

void mergeSort(node *firstElement, long int size);
node* divideSubroutine(node *todivide, long int size);
void merge(node *firstHalf, node *secondHalf, long int size);

node *head = NULL;
node *temp = NULL;

int main(void)
{
    ifstream fin;
    long int noOfElements;
    fin.open("IntegerArray.txt");
    if( !fin.is_open() )
    {
        cout << "COULD NOT OPEN THE FILE";
        return 0;
    }

    long int number;
    char noOfElements_[15];
    fin >> noOfElements_;
    noOfElements = atoi(noOfElements_);

    cout<<"\n\n The input array is as follows : \n\n";
    for (long int i = 0; i < noOfElements; i++)
    {
        char number_[15];
        fin >> number_;
        number = atoi(number_);
        cout << number << "\t";
        if (head == NULL)
        {
            head = new node;
            head->x = number;
            head->next = NULL;
            temp = head;

        }
        else
        {
            node *newnode = new node;
            newnode->next = NULL;
            newnode->x = number;
            temp->next = newnode;
            temp = temp->next;
        }


    }


    mergeSort(head, noOfElements);

    cout<<"\n\n The sorted array is as follows : \n\n";

    node *traversePtr = head;
    cout << endl;
    while(traversePtr != NULL)
    {
        cout << traversePtr->x << "\t";
        traversePtr = traversePtr->next;
    }
    cout<<endl<<endl;

}

void mergeSort(node *firstElement, long int size)
{
    if (size == 0)
    {
        return;
    }
    else
    {
        node *halfone = NULL;
        node *halftwo = NULL;
        halfone = firstElement;
        halftwo = divideSubroutine(firstElement, size);

        mergeSort( halfone, size / 2 );
        if (size % 2 == 1 && size != 1)
        {
            mergeSort( halftwo, ( size / 2 ) + 1 );
        }
        else
        {
            mergeSort( halftwo, size / 2 );
        }
        merge( halfone, halftwo, size );
    }



}

node* divideSubroutine(node *todivide, long int size)
{
    node *secondHalf = todivide;
    long int i = 0;
    while ( i < ( size / 2 ) )
    {
        secondHalf = secondHalf->next;
        i++;
    }
    return secondHalf;
}

void merge(node *firstHalf, node *secondHalf, long int size)
{
    long int i1 = 0;
    long int i2 = 0;
    long int size1 = size / 2;
    long int size2 = size / 2;
    if (size % 2 == 1 )
    {
        size2 = ( size / 2 ) + 1;
    }

    node *templl = NULL;
    node *temp1 = firstHalf;
    node *temp2 = secondHalf;
    node *templlptr = NULL;

    while(i1 != size1 && i2 != size2)
    {
        if( temp1->x <= temp2->x)
        {
            if(templl == NULL)
            {
                templl = new node;
                templl->x = temp1->x;
                templlptr = templl;
            }
            else
            {
                node *newnode = new node;
                newnode->x = temp1->x;
                newnode->next = NULL;
                templlptr->next = newnode;
                templlptr = templlptr->next;

            }

            i1++;
            temp1 = temp1->next;
        }
        else
        {
            if (templl == NULL)
            {
                templl = new node;
                templl->x = temp2->x;
                templlptr = templl;
            }
            else
            {
                node *newnode = new node;
                newnode->x = temp2->x;
                newnode->next = NULL;
                templlptr->next = newnode;
                templlptr = templlptr->next;

            }

            i2++;
            temp2 = temp2->next;
        }

    }
    if ( i1 != size1 )
    {
        while ( i1 != size1 )
        {
            if ( templl == NULL )
            {
                templl = new node;
                templl->x = temp1->x;
                templlptr = templl;
            }
            else
            {
                node *newnode = new node;
                newnode->x = temp1->x;
                newnode->next = NULL;
                templlptr->next = newnode;
                templlptr = templlptr->next;

            }

            i1++;
            temp1 = temp1->next;
        }
    }

    if ( i2 != size2 )
    {
        while ( i2 != size2 )
        {
            if ( templl == NULL )
            {
                templl = new node;
                templl->x = temp2->x;
                templlptr = templl;
            }
            else
            {
                node *newnode = new node;
                newnode->x = temp2->x;
                newnode->next = NULL;
                templlptr->next = newnode;
                templlptr = templlptr->next;

            }

            i2++;
            temp2 = temp2->next;
        }
    }

    long int i = 0;
    node *copy = templl;
    node *paste = firstHalf;
    while (i < size1 + size2)
    {
        paste->x = copy->x;
        copy = copy->next;
        paste = paste->next;
        i++;
    }

}
