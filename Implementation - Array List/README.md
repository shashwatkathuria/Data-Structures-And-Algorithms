# ARRAY LIST
--------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
--------------------------------


1. Run "./a.out" file.

2. The entries in the file are already inserted into the array.

3. The program is MENU-DRIVEN so you can appropriately operate on the array doing the
   operations that you want to do. e.g.->search,delete,sort,display,etc.


---------------------------
COMPONENTS OF THE FOLDER
---------------------------


1. "input.txt" file contains all the entries alongwith the number of entries on the

   top.

2. "personclasshelpers.h" is a user defined directory in which the class person is implemented.

3. "personarrayclasshelpers.h" is a user defined directory in which the class personarray
   is implemented.
   
4. "personarr.cpp" contains the main function.

5."./a.out" contains the compiled file compiled using g++ compiler.


------------------------------------------
TIME COMPLEXITIES
------------------------------------------


## 1) Class Person



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



## 2) Class PersonArray


  PersonArray()->

          O(1)

          complexity as takes constant number of steps to initialize length.


  void insertElementAtIndex(int index, Person element)->

          O(n)  [n=length of array]

          complexity as in worst case all the elements have to be shifted forward by 1.


  void deleteElementAtIndex(int index)->

          O(n)  [n=length of array]

          complexity as in worst case all the elements have to be shifted backward by 1.


  void display()->

          O(n)   [n=length of the array]

          complexity as all n elements inserted have to be displayed and displaying each element takes

          constant number of steps.


  void sort()->

          O(n^2)     [n=length of the array]

          complexity as bubble sort takes n^2 time in the worst case(when the array is in decending

          order).


  void searchForElement(Person p)->

          O(n)     [n-length of the array]

          complexity as in the worst case doesn't find the element after going through all the elements.



--------------------------------------------------------------------------------------

