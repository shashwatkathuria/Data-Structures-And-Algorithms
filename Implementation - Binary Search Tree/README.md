# BINARY SEARCH TREE
------------------------------------
INSTURCTIONS TO RUN THE PROGRAM
------------------------------------

1. Run ./a.out in the terminal to run the program and get the output.
2. The entries in the file "input.txt" is already inserted into the binary tree.
3. If you want to modify the entries, either modify the file "input.txt" or do
   the same with the help of the menu based interface of the program.

----------------
OUTPUTS
----------------

--)  "outputMenuBased.txt" contains the output of "BSTMenuBased.cpp".
--)  "outputTXTBased.txt" contains the output of "BSTOutputBased.cpp".
--)  "outputEmpiricalAnalysis.txt" contains the output of "BSTOutputBased.cpp".

------------------------------------
COMPONENTS OF THE PROGRAM
------------------------------------

a) BSTMenuBased---> || g++ BSTMenuBased.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the

        top.
        
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "bsthelpers.h" is a user defined directory in which the Class BinarySearchTree is implemented.
    4. "BSTMenuBased.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler.


------------------------------------
TIME COMPLEXITIES
------------------------------------



1) Class Person



  Person()->

          O(1)

          complexity as 2 strings(of max length 15) are copied alongwith age of person.


  Person(char fname[], char lname[], int a)->

          O(1)

          complexity as 2 strings(of max length 15) are copied alongwith age of person.


  void display()->

          O(1)

          complexity as name and age are printed which take constant number of steps.


  string getName()->

          O(1)

          complexity as firstname and lastname are max 15 length so takes constant number of steps.


  int getAge()->

          O(1)

          complexity as returns age which takes constant number of steps.


  void setAge()->

          O(1)

          complexity as sets age which takes constant number of steps.


  void setName()->

          O(1)

          complexity as sets name(2 strings of max 15 length) which takes constant number of steps.


  bool operator<(Person p)->

          O(1)

          complexity as takes constant number of steps to compare ages and firstnames(if ages are equal).


  bool operator>(Person p)->

          O(1)

          complexity as takes constant number of steps to compare ages and firstnames(if ages are equal).


  bool operator==(Person p)->

          O(1)

          complexity as takes constant number of steps to compare ages(if equal).


2) Class BinarySearchTree

  BinarySearchTree()-->
          
          O(1)
          
          complexity as points root to a new node and initializes no of elements to 0 which takes
          constant number of steps.

  bool search(node *dot, Person p)-->
          
          O(height)
          {
          	O(n)
          	complexity if the tree is imbalanced.
          	O(logn)
          	complexity if the tree is balanced(either partially or perfectly).
          }
          --Because in worst case goes down the height of the tree.
  
  void insert(node *dot, Person p)-->
          
          O(height)
          {
          	O(n)
          	complexity if the tree is imbalanced.
          	O(logn)
          	complexity if the tree is balanced(either partially or perfectly).
          }
          --Because in worst case goes down the height of the tree.

  void traversal(node *dot)-->
          
          O(n)
          complexity as prints each node of tree taking constant number of steps per node for displaying.

  bool deleteNode(node *dot, Person p)-->
          
          O(height)
          {
          	O(n)
          	complexity if the tree is imbalanced.
          	O(logn)
          	complexity if the tree is balanced(either partially or perfectly).
          }
          --Because in worst case goes down the height of the tree.

  node *predecessor(node *dot)-->
          
          O(height)
          {
          	O(n)
          	complexity if the tree is imbalanced.
          	O(logn)
          	complexity if the tree is balanced(either partially or perfectly).
          }
          --Because in worst case goes down the height of the tree.

  node *successor(node *dot)-->
          
          O(height)
          {
          	O(n)
          	complexity if the tree is imbalanced.
          	O(logn)
          	complexity if the tree is balanced(either partially or perfectly).
          }
          --Because in worst case goes down the height of the tree.

-------------------------------------------------------------------------------------------------------------------------------------
