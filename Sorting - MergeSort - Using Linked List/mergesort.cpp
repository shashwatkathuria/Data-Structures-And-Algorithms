#include<iostream>
#include<fstream>
#include<stdlib.h>

// MERGE SORT USING LINKED LIST

using namespace std;

// Defining node of linked list
struct node
{
    long int x;
    struct node *next;
};

// Declaring functions required
void mergeSort(node *firstElement, long int size);
node* divideSubroutine(node *todivide, long int size);
void merge(node *firstHalf, node *secondHalf, long int size);

node *head = NULL;
node *temp = NULL;

int main(void)
{
    // Reading input elements from the file and storing inside a linked list
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

    // Printing input array
    cout << "\n\n The input linked list is as follows : \n\n";
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

    // Calling merge sort algorithm on linked list
    mergeSort(head, noOfElements);

    // Printing final sorted linked list
    cout<<"\n\n The sorted linked list is as follows : \n\n";

    node *traversePtr = head;
    cout << endl;
    while(traversePtr != NULL)
    {
        cout << traversePtr->x << "\t";
        traversePtr = traversePtr->next;
    }
    cout << endl << endl;

}

void mergeSort(node *firstElement, long int size)
{
    // Base case
    if (size == 0)
    {
        return;
    }
    // Recursion case
    else
    {
        // Getting the pointer to the second half using divideSubroutine function
        node *halfone = NULL;
        node *halftwo = NULL;
        halfone = firstElement;
        halftwo = divideSubroutine(firstElement, size);

        // Calling merge sort on the two halves of the linked list and then merging them
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
    // Traversing half the size to get pointer to the second half of linked list
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
    // Declaring a new temporary linked lis for merging
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

    // Merging the two halves
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

    // Appending to the result the left out elements of left half
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

    // Appending to the result the left out elements of right half
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

    // Writing the elements of the temporary linked list(merged result) back into the original linked list
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
