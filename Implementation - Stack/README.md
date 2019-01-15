# STACK
------------------------------------
INSTURCTIONS TO RUN THE PROGRAM
------------------------------------

1. Run ./a.out in the terminal to run the program and get the output.
2. The entries in the file "input.txt" is already inserted into the stack.
3. If you want to modify the entries, either modify the file "input.txt" or do
   the same with the help of the menu based interface of the program.

----------------
OUTPUTS
----------------

--)  "outputStackMenuBased.txt" contains the output of "StackMenuBased.cpp".

------------------------------------
COMPONENTS OF THE PROGRAM
------------------------------------

a) StackMenuBased---> || g++ StackMenuBased.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the
         top.
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.
    3. "stackhelpers.h" is a user defined directory in which the Class Stack is implemented.
    4. "StackMenuBased.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler.


-----------------------------------
TIME COMPLEXITIES
------------------------------------



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


## 2) Class Stack

  Stack()-->

          O(1)
          complexity as points root to a new node and initializes no of elements(size) to 0 which takes
          constant number of steps.

  void push(Person p)-->

	      O(1)

	      complexity as it takes constant number of steps in general to insert at the top of the stack
  	      which involves pointer rewiring and some trivial steps.

  void pop()-->

	      O(1)

	      complexity as it takes constant number of steps in general to delete the top element of the stack
  	      which involves pointer rewiring and some trivial steps like displaying the person element which
          takes constant number of steps .

  void popwithoutdisplay()-->

	      O(1)

	      complexity as it takes constant number of steps in general to delete the top element of the stack
  	      which involves pointer rewiring and some trivial steps the only exception to the above method
          being that it doesn't display the person element.

  void search(Person p)-->

	      O(n)

	      complexity as in the worst case the element is not in the stack and we have to pop out
          all the n elements which takes constant steps per element.

  void displayStack()-->

          O(n)

          complexity as prints each element of stack taking constant number of steps per element for
          displaying.

  void deleteStack()-->

	      O(n)

 	      complexity as it deletes all n elements of the stack which takes constant number of steps per
 	      element.


-------------------------------------------------------------------------------------------------------------------------------------
