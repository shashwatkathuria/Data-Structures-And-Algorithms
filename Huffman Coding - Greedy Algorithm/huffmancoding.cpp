#include<iostream>
#include<fstream>

using namespace std;

// HUFFMAN CODING ALGORITHM - GREEDY ALGORITHM

// Defining node beacuse it will be the basic component of the tree class
struct node
{
    unsigned long long int frequency;
    int nodeNumber;
    struct node* parent;
    struct node* leftChild;
    struct node* rightChild;

};

// Defining class Tree
class Tree
{
    public:
      node *root ;

      // Constructor for class tree, starts with defining a single node only
      Tree (int nodeNumber = 0, long long int frequency = 0)
      {
          root = new node;
          root->parent = NULL;
          root->leftChild = NULL;
          root->rightChild = NULL;
          root->frequency = frequency;
          root->nodeNumber = nodeNumber;
      }

      // Functions required for the algorithm
      void treeMerger(Tree& tree);
      void printCodes(node* element, string str);
      unsigned long long int nodesSum(node* element);
      unsigned long long int minDepth(node* element);
      unsigned long long int maxDepth(node* element);

};


int main(void)
{
    // Reading node frequencies from the input file and storing inside an array
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

    cout << "The number of nodes present are : " << noOfElements << endl;

    // Defining a tree array, of which each element is for each of the individual nodes
    // For now, default initializing, to be modified in next for loop
    // To be merged later
    Tree treeCandidates[noOfElements];

    // Initializing each tree in the tree array with specific node number and details
    for(int i = 0; i < noOfElements; i++)
    {
        // Node number of individual node tree
        treeCandidates[i].root->nodeNumber = i + 1;

        // Frequency of individual node tree
        treeCandidates[i].root->frequency = freqs[i];
    }

    // Initializing minimum candidates and their positions for the sake of it, as such does not have any meaning
    Tree firstMinimumCandidate = treeCandidates[0];
    Tree secondMinimumCandidate = treeCandidates[1];
    int firstMinimumCandidatePosition = 0;
    int secondMinimumCandidatePosition = 1;

    // Number of elements to be analyzed after each iteration, pushing duplicate trees at end of array
    // so that they don't interfere with the algorithm minimum frequency trees computation
    int posEnd = noOfElements - 1;

    // Merging number of elements - 1 times so as to get the final tree in the end at 0th index
    // Merging two minimum frequency trees in each iteration
    for (int j = 0; j < noOfElements - 1; j++)
    {

      // Defining the two minimum candidates in such a way so as to get the two smallest minimum frequency trees

      // 1st Smallest frequency tree
      Tree firstMinimumCandidate = Tree(0, 99999999999999);
      // 2nd Smallest frequency tree
      Tree secondMinimumCandidate = Tree(0, 999999999999);

      // Getting 1st Smallest frequency tree
      for (int i = 0; i <= posEnd; i++)
      {
          if (treeCandidates[i].nodesSum(treeCandidates[i].root) < firstMinimumCandidate.nodesSum(firstMinimumCandidate.root))
          {
              firstMinimumCandidate = treeCandidates[i];
              firstMinimumCandidatePosition = i;
          }
      }

      // Getting 2nd Smallest frequency tree
      for (int i = 0; i <= posEnd; i++)
      {
          // Second condition ensures that we get the 2nd smallest frequency tree as it is smaller than all trees but
          // not equal to the 1st smallest frequency tree
          if ( (treeCandidates[i].nodesSum(treeCandidates[i].root) < secondMinimumCandidate.nodesSum(secondMinimumCandidate.root)) && (treeCandidates[i].nodesSum(treeCandidates[i].root) != firstMinimumCandidate.nodesSum(firstMinimumCandidate.root)) )
          {
              secondMinimumCandidate = treeCandidates[i];
              secondMinimumCandidatePosition = i;
          }
      }

      // Merging the candidates
      secondMinimumCandidate.treeMerger(firstMinimumCandidate);

      // Updating the tree array with the new modified version
      treeCandidates[firstMinimumCandidatePosition] = firstMinimumCandidate;
      treeCandidates[secondMinimumCandidatePosition] = secondMinimumCandidate;

      // Pushing one duplicate to end as both trees correspond to their same merged versions
      Tree temp = treeCandidates[posEnd];
      treeCandidates[posEnd] = treeCandidates[secondMinimumCandidatePosition];
      treeCandidates[secondMinimumCandidatePosition] = temp;

      // As a new duplicate is pushed to end, we decrement end position so that we don't compute on duplicates
      posEnd--;

    }

    // Printing the results
    cout << "Sum of frequency of nodes : " << treeCandidates[0].nodesSum(treeCandidates[0].root);
    cout << endl;
    treeCandidates[0].printCodes(treeCandidates[0].root, "");
    cout << endl << "The minimum depth of the tree is : " << treeCandidates[0].minDepth(treeCandidates[0].root) << endl;
    cout << endl << "The maximum depth of the tree is : " << treeCandidates[0].maxDepth(treeCandidates[0].root) << endl;

    return 0;
}

// Function to compute the sum of node frequencies in tree recursively
unsigned long long int Tree:: nodesSum(node* element)
{
    // Base case
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        return element->frequency;
    }

    // Getting the sum of left and right subtrees under any intermediate node considered as a tree
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        return nodesSum(element->rightChild) + nodesSum(element->leftChild);
    }

}

// Function to merge two trees
void Tree:: treeMerger(Tree& tree)
{
    // Merging in such a way that each node in tree will have either
    // no children (base case initialization of tree) or two children
    // This is why the recursive functions have no cases for one child
    node* temp = new node;

    // Internal node will not contribute to sum of frequencies
    // which is why its frequency is kept 0
    temp->frequency = 0;

    // Pointer rewiring
    temp->leftChild = root;
    temp->rightChild = tree.root;
    root-> parent = temp;
    tree.root-> parent = temp;
    root = temp;
    tree.root = temp;

}

// Function to compute minimum depth of tree recursively
unsigned long long int Tree:: minDepth(node* element)
{
    // Base Case
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        return 0;
    }

    // Extracting minimum depth at each node
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        return min( minDepth(element->rightChild), minDepth(element->leftChild) ) + 1;
    }
}

// Function to compute maximum depth of tree recursively
unsigned long long int Tree:: maxDepth(node* element)
{
    // Base Case
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        return 0;
    }

    // Extracting minimum depth at each node
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        return max( maxDepth(element->rightChild), maxDepth(element->leftChild) ) + 1;
    }
}

// Function to print the optimal huffman codes for each of the nodes recursively
void Tree:: printCodes(node* element, string str)
{
    // Base Case
    if ( (element-> leftChild == NULL) && (element-> rightChild == NULL) )
    {
        cout << "Node Number " << element->nodeNumber << " Code : " << str << "\n";
        return;
    }

    // Appending 0 for the huffman code of left child and 1 for the huffman code of right child
    else if ( (element-> leftChild != NULL) && (element-> rightChild != NULL) )
    {
        printCodes(element->leftChild, str + "0");
        printCodes(element->rightChild, str + "1");
    }
}
