#include<iostream>
using namespace std;
struct node
{
    Person p;
    struct node *down;
};
class Stack
{
    public:
        node *top;
        int size;
        void push(Person p);
        void pop();
        void popwithoutdisplay();
        void displayStack();
        void deleteStack();
        void search(Person p);
        Stack()
        {
            size=0;
            top=NULL;
        }

};

void Stack::push(Person p)
{
    if(size==0)
    {
        node *temp=new node;
        temp->p=p;
        temp->down=NULL;
        top=temp;
        size++;
    }
    else
    {
        node *temp=new node;
        temp->p=p;
        temp->down=top;
        top=temp;
        size++;
    }
}

void Stack::pop()
{
    if(size==0)
    {
        cout<<"NO ELEMENTS IN STACK!!!CANNOT DELETE ANYTHING!!";
        return;
    }
    else
    {
        cout<<endl;
        cout<<"DELETING THE ELEMENT";
        (top->p).display();
        if ((size-1)==0)
        {
            top=NULL;
            size--;
        }
        else
        {
            top=top->down;
            size--;
        }

    }
}

void Stack::displayStack()
{
    if(size==0)
    {
        cout<<"NO ELEMENTS IN THE STACK!!CANNOT DISPLAY THE STACK!!";
    }
    else
    {
        cout<<"DISPLAYING THE STACK FROM TOP TO BOTTOM.."<<endl<<endl;
        int i=0;
        node *traverse=top;
        while(traverse!=NULL)
        {
            cout<<"ELEMENT AT "<<i<<" PLACES FROM TOP =";
            (traverse->p).display();
            cout<<endl;
            traverse=traverse->down;
            i++;
        }
    }
}

void Stack::search(Person p)
{
    if(size==0)
    {
        cout<<"NO ELEMENTS IN THE STACK!!CANNOT SEARCH FOR ANYTHING!!";
        return;
    }
    else
    {
        Stack temp;
        cout<<endl<<"SEARCHING....";
        cout<<endl<<"USING TEMPORARY STACK WHILE SEARCHING(AND POPPING FROM ORIGINAL STACK)....";
        node *found=NULL;
        int i=0;
        while(top!=NULL)
        {
            temp.push(top->p);
            popwithoutdisplay();
            if((strcmpi((temp.top->p).firstname, p.firstname) == 0) && (strcmpi((temp.top->p).lastname, p.lastname) == 0) && ((temp.top->p).getAge() == p.getAge()))
            {

                found=temp.top;
                break;

            }
            i++;
        }

        cout<<endl<<"PUSHING ELEMENTS SEARCHED BACK INTO ORIGINAL STACK...."<<endl;
        while(temp.top!=NULL)
        {
            push(temp.top->p);
            temp.popwithoutdisplay();
        }
        if(found==NULL)
        {
            cout<<"GIVEN ELEMENT NOT IN STACK!!"<<endl;
        }
        else
        {
            cout<<endl;
            cout<<"FOUND THE ELEMENT AT "<<i<<" POSITIONS FROM TOP";
            (found->p).display();
            cout<<endl;

        }


        return;
    }
}

void Stack::popwithoutdisplay()
{
    if(size==0)
    {
        cout<<"NO ELEMENTS IN STACK!!!CANNOT DELETE ANYTHING!!";
        return;
    }
    else
    {
        if ((size-1)==0)
        {
            top=NULL;
            size--;
        }
        else
        {
            top=top->down;
            size--;
        }

    }

}

void Stack::deleteStack()
{
    while(size!=0)
    {
        popwithoutdisplay();
    }
    cout<<endl<<"SUCCESSFULLY DELETED WHOLE STACK!!"<<endl;

}