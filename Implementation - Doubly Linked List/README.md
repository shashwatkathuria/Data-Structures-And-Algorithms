--------------------------------

# INSTRUCTIONS TO RUN THE PROGRAM

--------------------------------


1.Run "./a.out" file.


2.The entries in the file are already inserted into the doubly linked list.


3.The program is MENU-DRIVEN so you can appropriately operate on the doubly linked list doing the

  operations that you want to do. e.g.->search,delete,sort,display,etc.


---------------------------

# COMPONENTS OF THE FOLDER

---------------------------


1."input.txt" file contains all the entries alongwith the number of entries on the

  top(as mentioned in google classroom).[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO

  MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]


2."personclasshelpers.h" is a user defined directory in which the class person is implemented.


3."persondllclasshelpers.h" is a user defined directory in which the class persondoublylinkedlist

  is implemented.


4."persondll.cpp" contains the main function.


5."./a.out" contains the compiled file compiled using g++ compiler.


---------------------------------------------

# TIME COMPLEXITIES

---------------------------------------------



# 1) Class Person



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



# 2) Class PersonDoublyLinkedList



  PersonDoublyLinkedList()->

          O(1)

          complexity as takes constant number of steps to initialize length to 0 and root to NULL.


  void insertNode(Person p)->

          O(1)

          complexity as takes constant number of steps to attach the new person to the starting

          of the list.


  void traverseList()->

          O(n)   [n=length of the doubly linked list]

          complexity as all n elements inserted have to be displayed and displaying each element takes

          constant number of steps.


  void searchNode(Person p)->

          O(n)     [n=length of the doubly linked list]

          complexity as in the worst case doesn't find the element after going through all the elements.


  void deleteNode(Person p)->

          O(n)  [n=length of doubly linked list]

          complexity as in worst case goes through each element of the list before hitting the end

          of the list to delete the element at the last or doesn't find the element to be deleted

          in the list.


  void sort()->

          O(n^2)     [n=length of the doubly linked list]

          complexity as bubble sort takes n^2 time in the worst case(when the doubly linked list is in

          descending order).


  void deleteWholeDLL()->

          O(n)       [n=length of the doubly linked list]

          complexity as goes through each element in the list one by one to delete them(which takes

          constant number of steps per element).


------------------##---------------------------------##-----------------------------------
