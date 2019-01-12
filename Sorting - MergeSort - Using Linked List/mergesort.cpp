#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
struct node
{
    long int   x;
    struct node *next;
};


void mergeSort(node *firstelement,long int   size);
node* divideSubroutine(node *todivide, long int   size);
void merge(node *firsthalf, node *secondhalf, long int   size);

node *head=NULL;
node *temp=NULL;
int  main(void)
{
    ifstream fin;
    long int   n;
    fin.open("IntegerArray.txt");
    if(!fin.is_open())
    {
        cout<<"COULD NOT OPEN THE FILE";
        return 0;
    }
    long int   number;
    char noofelements[15];
    fin>>noofelements;
    n=atoi(noofelements);
    // n=6;
    // n=100000;
    for (long int   i=0; i<n; i++)
    {
        char number_[15];
        fin>>number_;
        number=atoi(number_);
        // cout<<endl<<number;
        if(head==NULL)
        {
            head=new node;
            head->x=number;
            head->next=NULL;
            temp=head;

        }
        else
        {
            node *newnode=new node;
            newnode->next=NULL;
            newnode->x=number;
            temp->next=newnode;
            temp=temp->next;
        }


    }


    mergeSort(head,n);

    node *traverse=head;
    cout<<endl;
    while(traverse!=NULL)
    {
        cout<<traverse->x<<endl;
        traverse=traverse->next;
    }
}

void mergeSort(node *firstelement, long int   size)
{
    if(size==0)
    {
        return;
    }
    else
    {
        node *halfone = NULL;
        node *halftwo = NULL;
        halfone=firstelement;
        halftwo=divideSubroutine(firstelement, size);

        mergeSort(halfone,size/2);
         if(size%2==1 && size!=1)
            mergeSort(halftwo,(size/2)+1);
         else
            mergeSort(halftwo,size/2);
        //if(size!=1)
           merge(halfone, halftwo,size);
    }

}

node* divideSubroutine(node *todivide, long int   size)
{
    node *secondhalf=todivide;
    long int   i=0;
    while(i<(size/2))
    {
        secondhalf=secondhalf->next;
        i++;
    }
    return secondhalf;
}

void merge(node *firsthalf, node *secondhalf, long int   size)
{
    long int   i1=0;
    long int   i2=0;
    long int   size1=size/2;
    long int   size2=size/2;
    if(size % 2 == 1 )//&& size!=1)
    {
        size2=(size/2)+1;
    }
    // cout<<endl<<"-------"<<endl;
    // cout<<" "<<size1<<" "<<size2;
    // cout<<endl;
    node *templl=NULL;
    node *temp1=firsthalf;
    node *temp2=secondhalf;
    node *templlptr=NULL;

    while(i1!=size1 && i2!=size2)
    {
        // cout<<endl;
        // cout<<" "<<temp1->x<<" "<<temp2->x;
        // cout<<endl;
        // cout<<" "<<i1<<" "<<i2;
        // cout<<endl;


        if( temp1->x <= temp2->x)
        {
            if(templl==NULL)
            {
                templl=new node;
                templl->x=temp1->x;
                templlptr=templl;
            }
            else
            {
                node *newnode=new node;
                newnode->x=temp1->x;
                newnode->next=NULL;
                templlptr->next=newnode;
                templlptr=templlptr->next;

            }

            i1++;
            temp1=temp1->next;
        }
        else
        {
            if(templl==NULL)
            {
                templl=new node;
                templl->x=temp2->x;
                templlptr=templl;
            }
            else
            {
                node *newnode=new node;
                newnode->x=temp2->x;
                newnode->next=NULL;
                templlptr->next=newnode;
                templlptr=templlptr->next;

            }

            i2++;
            temp2=temp2->next;
        }

        // cout<<" "<<i1<<" "<<i2;
        // cout<<endl;
        // cout<<"------";
    }
    if(i1!=size1)
    {
        while(i1!=size1)
        {
            // cout<<endl<<" "<<temp1->x;
            if(templl==NULL)
            {
                templl=new node;
                templl->x=temp1->x;
                templlptr=templl;
            }
            else
            {
                node *newnode=new node;
                newnode->x=temp1->x;
                newnode->next=NULL;
                templlptr->next=newnode;
                templlptr=templlptr->next;

            }

            i1++;
            temp1=temp1->next;
        }
    }

    if(i2!=size2)
    {
        while(i2!=size2)
        {
//            cout<<endl<<" "<<temp2->x<<endl;
            if(templl==NULL)
            {
                templl=new node;
                templl->x=temp2->x;
                templlptr=templl;
            }
            else
            {
                node *newnode=new node;
                newnode->x=temp2->x;
                newnode->next=NULL;
                templlptr->next=newnode;
                templlptr=templlptr->next;

            }

            i2++;
            temp2=temp2->next;
        }
    }

    long int   i=0;
    node *copy=templl;
    node *paste=firsthalf;
    // cout<<endl;
    while(i < size1+size2)
    {
        // cout<<copy->x<<"  ";
        paste->x=copy->x;
        copy=copy->next;
        paste=paste->next;
        i++;
    }



}

