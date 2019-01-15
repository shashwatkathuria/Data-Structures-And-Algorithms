_____________________
SHASHWAT KATHURIA
B17CS050
CSE BRANCH
6TH SEPTEMBER 2018
ASSIGNMENT 3
_____________________

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
--)  "outputStackTXTBased.txt" contains the output of "StackOutputTXTBased.cpp".
--)  "outputEmpiricalAnalysis.txt" contains the output of "empiricalanalysis.cpp".
_______________________________________________________________________________________
------------------------------------
COMPONENTS OF THE PROGRAM
------------------------------------

a)StackMenuBased---> || g++ StackMenuBased.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the

        top(as mentioned in google classroom).[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO

   	MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "stackhelpers.h" is a user defined directory in which the Class Stack is implemented.
    4. "StackMenuBased.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler.



b)StackOutputTXTBased---> || g++ StackOutputTXTBased.cpp ||

    1.  "input.txt" file contains all the entries alongwith the number of entries on the

        top(as mentioned in google classroom).[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO

   	MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]
    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "stackhelpers.h" is a user defined directory in which the Class Stack is implemented.
    4. "StackOutputTXTBased.cpp" contains the main function.
    5. "./a.out" contains the compiled file compiled using g++ compiler.



c)EmpiricalAnalysis---> || g++ -std=c++11 empiricalanalysis.cpp ||

    1.  "input.txt" file contains large number of entries alongwith the number of entries on the

        top.[IF YOU WANT TO ALTER THE FILE,PLEASE DONT FORGET TO MODIFY THE NUMBER OF ENTRIES ON THE TOP OF THE FILE]

    2. "personclasshelpers.h" is a user defined directory in which the Class Person is implemented.

    3. "stackhelpers.h" is a user defined directory in which the Class Stack is implemented.

    4. "empiricalanalysis.cpp" contains the main function.

    5. "./a.out" contains the compiled file compiled using g++ compiler and c++11 standard.

    6. "chrono.h" library is used to measure time differences and intervals.


---------------------------------------------------------------------------------------------------------------
EXPLANATION OF OUTPUT OF "EMPIRICALANALYSIS.CPP" [LARGE INPUT TAKEN]
---------------------------------------------------------------------------------------------------------------

1) The ratio is around 2 as during the iteration I call displayStack() 2 times, once the Stack is halfly
   inserted and one when it is fully inserted so it follows from o(n) complexity that the ratio will be
   close to 2.

2) The ratio is close to 5 as I invoke search() on two persons who take 1000 and 200  proportionate steps
   so it follows that because of the O(n) complexity the ratio will be 5.

3) The ratio is around 1 as I invoke pop() which has O(1) time complexity so it takes approximately the same
   number of steps for all elements.

4) The ratio is around 1 as I invoke deleteStack() on two stacks containing the same number of elements so
   it follows from the O(n) complexity that the ratio will be close to 1.

5) The average number of steps taken by push() is also outputted as it has O(1) complexity.

6) The other functions involving class Person respectively take O(1) constant time as is displayed by almost
   every other person entry which takes a constant number of steps.

----------------------------------------------------------------------------------------------------------------
-----------------------------------
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


2)Class Stack

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


----------------------------------X--------------------------------------X-------------------------------------------------------------