#include<iostream>
#include<fstream>

using namespace std;

struct node
{
    unsigned long long int frequency;
    int nodeNumber;
    struct node* parent;
    struct node* leftChild;
    struct node* rightChild;

};
int leftHeight = 0;
int rightHeight = 0;
class Tree
{
    public:
      node *root ;
      Tree (int nodeNumber = 0, long long int frequency = 0)
      {
          root = new node;
          root->parent = NULL;
          root->leftChild = NULL;
          root->rightChild = NULL;
          root->frequency = frequency;
          root->nodeNumber = nodeNumber;
      }
      unsigned long long int nodesSum(node* element);
      void treeMerger(Tree& tree);
      void treeHeight();
      unsigned long long int minDepth(node* element);
      unsigned long long int maxDepth(node* element);
      void printCodes(node* element, string str);
};


int main(void)
{

      ifstream fin;
      long int noOfElements;
      fin.open("huffmanNodeFrequencies.txt");
      if( !fin.is_open() )
      {
          cout << "COULD NOT OPEN THE FILE";
          return 0;
      }

      long int number;
      char noOfElements_[15];
      fin >> noOfElements_;
      noOfElements = atoi(noOfElements_);
      long long int freqs[noOfElements];
      unsigned long long int sum = 0;
      for (long int i = 0; i < noOfElements; i++)
      {
          char number_[15];
          fin >> number_;
          number = atoi(number_);
          freqs[i] = number;

      }
      cout << noOfElements << endl;

    Tree treeCandidates[noOfElements];

    for(int i = 0; i < noOfElements; i++)
    {
        treeCandidates[i].root->nodeNumber = i + 1;
        treeCandidates[i].root->frequency = freqs[i];
    }

    Tree firstMinimumCandidate = treeCandidates[0];
    Tree secondMinimumCandidate = treeCandidates[1];
    int pos1 = 0;
    int pos2 = 1;
    int posEnd = noOfElements - 1;

    for (int j = 0; j < noOfElements - 1; j++)
    {
      cout<<endl;
      Tree firstMinimumCandidate = Tree(0, 99999999999999);
      Tree secondMinimumCandidate = Tree(0, 999999999999);

      for (int i = 0; i <= posEnd; i++)
      {
          if (treeCandidates[i].nodesSum(treeCandidates[i].root) < firstMinimumCandidate.nodesSum(firstMinimumCandidate.root))
          {
              firstMinimumCandidate = treeCandidates[i];
              pos1 = i;
          }
      }

      for (int i = 0; i <= posEnd; i++)
      {
          if ( (treeCandidates[i].nodesSum(treeCandidates[i].root) < secondMinimumCandidate.nodesSum(secondMinimumCandidate.root)) && (treeCandidates[i].nodesSum(treeCandidates[i].root) != firstMinimumCandidate.nodesSum(firstMinimumCandidate.root)) )
          {
              secondMinimumCandidate = treeCandidates[i];
              pos2 = i;
          }
      }

      secondMinimumCandidate.treeMerger(firstMinimumCandidate);

      treeCandidates[pos1] = firstMinimumCandidate;
      treeCandidates[pos2] = secondMinimumCandidate;

      Tree temp = treeCandidates[posEnd];
      treeCandidates[posEnd] = treeCandidates[pos2];
      treeCandidates[pos2] = temp;
      posEnd--;

    }

    cout << treeCandidates[0].nodesSum(treeCandidates[0].root);
    cout << endl;
    treeCandidates[0].printCodes(treeCandidates[0].root, "");

    cout << endl << "The minimum depth of the tree is : " << treeCandidates[0].minDepth(treeCandidates[0].root) << endl;
    cout << endl << "The maximum depth of the tree is : " << treeCandidates[0].maxDepth(treeCandidates[0].root) << endl;
    return 0;
}

unsigned long long int Tree:: nodesSum(node* element)
{
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        return element->frequency;
    }
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        return nodesSum(element->rightChild) + nodesSum(element->leftChild);
    }

}

void Tree:: treeMerger(Tree& tree)
{

    node* temp = new node;
    temp->frequency = 0;
    temp->leftChild = root;
    temp->rightChild = tree.root;
    root-> parent = temp;
    tree.root-> parent = temp;
    root = temp;
    tree.root = temp;

}
unsigned long long int Tree:: minDepth(node* element)
{
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        return 0;
    }
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        return min( minDepth(element->rightChild), minDepth(element->leftChild) ) + 1;
    }
}

unsigned long long int Tree:: maxDepth(node* element)
{
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        return 0;
    }
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        return max( maxDepth(element->rightChild), maxDepth(element->leftChild) ) + 1;
    }
}

void Tree:: printCodes(node* element, string str)
{
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        cout << "Node Number " << element->nodeNumber << " Code : " << str << "\n";
        return;
    }
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        printCodes(element->leftChild, str + "0");
        printCodes(element->rightChild, str + "1");
    }
}
