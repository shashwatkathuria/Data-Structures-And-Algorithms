#include<iostream>
// #include<fstream>

using namespace std;

struct node
{
    long long int frequency;
    int nodeNumber;
    struct node* parent;
    struct node* leftChild;
    struct node* rightChild;

};
node* root = new node;
int main(void)
{
  int noOfElements = 5;

  node n1 = new node;
  n1.frequency = 1;
  n1.nodeNumber = 1;
  n1.parent = NULL;
  n1.rightChild = NULL;
  n1.leftChild = NULL;

  node n2 = new node;
  n2.frequency = 2;
  n2.nodeNumber = 2;
  n2.parent = NULL;
  n2.rightChild = NULL;
  n2.leftChild = NULL;

  node n3 = new node;
  n3.frequency = 3;
  n3.nodeNumber = 3;
  n3.parent = NULL;
  n3.rightChild = NULL;
  n3.leftChild = NULL;

  node n4 = new node;
  n4.frequency = 4;
  n4.nodeNumber = 4;
  n4.parent = NULL;
  n4.rightChild = NULL;
  n4.leftChild = NULL;

  node n5 = new node;
  n5.frequency = 5;
  n5.nodeNumber = 5;
  n5.parent = NULL;
  n5.rightChild = NULL;
  n5.leftChild = NULL;

  node* parent = new node;
  parent -> leftChild = n1;
  parent -> rightChild = n2;
  // get pointers of two subtrees with minimum frequencies;
  // merge them;

  return 0;
}
