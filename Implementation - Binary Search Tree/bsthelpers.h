#include<iostream>
using namespace std;

struct node
{
    Person p;
    struct node *parent;
    struct node *leftchild;
    struct node *rightchild;
};

class BinarySearchTree
{
    public:
        node *root;
        int noofelements;
        BinarySearchTree()
        {
            root = new node;
            noofelements = 0;
        }
        bool search(node *dot, Person p);
        void insert(node *dot, Person p);
        void traversal(node *dot);
        bool deleteNode(node *dot, Person p);
        node *predecessor(node *dot);
        node *successor(node *dot);

};

bool BinarySearchTree:: search(node *dot, Person p)
{
    if (dot == NULL)
    {
        cout<<"NOT FOUND";
        return false;
    }
    else if ((strcmpi((dot->p).firstname, p.firstname) == 0) && (strcmpi((dot->p).lastname, p.lastname) == 0) && ((dot->p).getAge() == p.getAge()))
    {
        cout<<endl;
        cout<<"FOUND";
        (dot->p).display();
        return true;
    }
    else
    {
        if (p < dot->p)
        {
            return search(dot->leftchild, p);
        }
        else if (p > dot->p)
        {
            return search(dot->rightchild, p);
        }
    }

}

void BinarySearchTree:: insert(node *dot, Person p)
{
    static int i = 0;
    if (i == 0)
    {
        root->p = p;
        i++;
        cout<<endl;
        traversal(root);
        cout<<endl;
        noofelements++;
        return;
    }

    if(p < dot->p)
    {
        if(dot->leftchild==NULL)
        {
            node *temp = new node;
            temp->p = p;
            temp->leftchild = NULL;
            temp->rightchild = NULL;
            temp->parent = dot;
            dot->leftchild = temp;
            cout<<endl;
            traversal(root);
            cout<<endl;
            noofelements++;
            return;
        }
        else
        {
            insert(dot->leftchild,p);
        }
    }
    else if(p > dot->p)
    {
        if(dot->rightchild == NULL)
        {
            node *temp = new node;
            temp->p = p;
            temp->leftchild = NULL;
            temp->rightchild = NULL;
            temp->parent = dot;
            dot->rightchild = temp;
            cout<<endl;
            traversal(root);
            cout<<endl;
            noofelements++;
            return;
        }
        else
        {
            insert(dot->rightchild, p);
        }
    }
}

void BinarySearchTree::traversal(node *dot)
{
    if(dot == NULL)
    {
        return;
    }
    else
    {
        traversal(dot->leftchild);
        cout<<" ";
        (dot->p).display();
        cout<<" ";
        traversal(dot->rightchild);
    }
}

bool BinarySearchTree::deleteNode(node *dot,Person p)
{
    if (dot == NULL)
    {
        return false;
    }
    else if ((strcmpi((dot->p).firstname, p.firstname) == 0) && (strcmpi((dot->p).lastname, p.lastname) == 0) && ((dot->p).getAge() == p.getAge()))
    {
        if(dot->leftchild != NULL && dot->rightchild!=NULL)
        {
            node *temp = predecessor(dot);
            Person temp1 = temp->p;
            temp->p = dot->p;
            dot->p = temp1;
            return deleteNode(temp,p);
        }
        else if (dot->leftchild == NULL && dot->rightchild != NULL)
        {
            if(dot->parent->leftchild == dot)
            {
                dot->parent->leftchild = dot->rightchild;
                dot->rightchild->parent = dot->parent;
                dot->rightchild = NULL;
                dot->parent = NULL;
            }
            else if(dot->parent->rightchild == dot)
            {
                dot->parent->rightchild = dot->rightchild;
                dot->rightchild->parent = dot->parent;
                dot->rightchild = NULL;
                dot->parent = NULL;
            }
            noofelements--;
            return true;
        }
        else if(dot->leftchild != NULL && dot->rightchild == NULL)
        {
            if(dot->parent->leftchild == dot)
            {
                dot->parent->leftchild = dot->leftchild;
                dot->leftchild->parent = dot->parent;
                dot->leftchild = NULL;
                dot->parent = NULL;
            }
            else if(dot->parent->rightchild == dot)
            {
                dot->parent->rightchild = dot->leftchild;
                dot->leftchild->parent = dot->parent;
                dot->leftchild = NULL;
                dot->parent = NULL;
            }
            noofelements--;
            return true;
        }
        else
        {
            if(dot->parent->leftchild == dot)
            {
                dot->parent->leftchild = NULL;
                dot->parent = NULL;
            }
            else if(dot->parent->rightchild == dot)
            {
                dot->parent->rightchild = NULL;
                dot->parent = NULL;
            }
            noofelements--;
            return true;
        }

    }
    else
    {
        if(p < dot->p)
        {
            return deleteNode(dot->leftchild, p);
        }
        else if(p > dot->p)
        {
            return deleteNode(dot->rightchild, p);
        }
    }

}

node* BinarySearchTree::predecessor(node *dot)
{
    node *k = dot->leftchild;
    while (k->rightchild != NULL)
    {
        node *temp = k->rightchild;
        if (temp != NULL)
        {
            k = temp;
        }
        else
        {
            break;
        }
    }
    return k;
}
node* BinarySearchTree::successor(node *dot)
{
    node *k = dot->rightchild;
    while (k->leftchild != NULL)
    {
        node *temp = k->leftchild;
        if (temp != NULL)
        {
            k = temp;
        }
        else
        {
            break;
        }
    }
    return k;
}