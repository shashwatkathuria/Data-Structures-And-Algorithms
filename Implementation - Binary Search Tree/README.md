_____________________
SHASHWAT KATHURIA
B17CS050
CSE BRANCH
30TH AUGUST 2018
ASSIGNMENT 2
_____________________

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
_______________________________________________________________________________________
------------------------------------
COMPONENTS OF THE PROGRAM
------------------------------------

a)BSTMenuBased---> || g++ BSTMenuBased.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the

        top(as mentioned in google classroom).[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO

   	MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "bsthelpers.h" is a user defined directory in which the Class BinarySearchTree is implemented.
    4. "BSTMenuBased.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler.



b)BSTOutputTXTBased---> || g++ BSTOutputTXTBased.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the

        top(as mentioned in google classroom).[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO

   	MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "bsthelpers.h" is a user defined directory in which the Class BinarySearchTree is implemented.
    4. "BSTOutputTXTBased.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler.



c)EmpiricalAnalysis---> || g++ -std=c++11 empiricalanalysis.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the

        top(as mentioned in google classroom).[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO

   	MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "bsthelpers.h" is a user defined directory in which the Class BinarySearchTree is implemented.
    4. "empiricalanalysis.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler and c++11 standard.

    6. "chrono.h" library is used to measure time differences and intervals.

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


2)Class BinarySearchTree

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
---------------------------------------------------------------------------------------------------------------
EXPLANATION OF OUTPUT OF "EMPIRICALANALYSIS.CPP" [INPUT IS SUCH THAT A O(n) skewed binary search tree is made]
---------------------------------------------------------------------------------------------------------------
1) The ratio is around 2 as during the iteration I call traversal 2 times, once the BST if halfly inserted and
   one when it is fully inserted so it follows from o(n) complexity that the ratio will be close to 2.
2) The ratio is close to 1 as I invoke search on two persons who are neighbours to each other in the skewed binary
   tree so it follows that because of the O(n) complexity the ratio will be 1.
3) The ratio is around 6 as I invoke deleteNode() on instances which take 3 and 19 steps in proportion to be
   deleted respectively so it automatically follows from O(n) complexity that the ratio will be around 6 due to
   skewed nature of the tree and O(n) complexity.
4) The other functions respectively take O(1) constant time as is displayed by almost every other person entry
   involving a constant number of steps.

----------------------------------X--------------------------------------X-------------------------------------------------------------