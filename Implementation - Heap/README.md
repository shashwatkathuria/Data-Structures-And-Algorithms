
# MINHEAP AND MAXHEAP
------------------------------------
# INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------
1. Run ./a.out in the terminal to run the program and get the output.

2. The entries in the file "input.txt" are inserted alongwith the number of entries at the top.

----------------
# OUTPUT
----------------
--)  "output.txt" contains the output of "heap.cpp".

------------------------------------
# COMPONENTS OF THE FILE
------------------------------------

--) || g++ heap.cpp ||

    1.  "input.txt" file contains numbers to be inserted into heap alongwith
	number of entries at the top.

    2. "./a.out" contains the compiled file compiled using g++ compiler.

    3. "heap.cpp" is the program written in C++.

    4. "output.txt" contains the output of the program.


-----------------------------------
# TIME COMPLEXITIES
------------------------------------

class minHeap and class maxHeap

1) minHeap() // maxHeap()

          O(1)

          complexity because initializing the two data members takes constant
          number of steps.

2) void printTop3Rows()

          O(1)

          complexity as printing the top 3 rows takes constant number of steps.

3) int extractRoot()
          
	   O(1)       
	  
	   complexity as returning 1st element takes constant number of steps.

4) void removeRoot()
          
	   O(height)     height = logn if balanced heap |||between logn -> n in general

           complexity as takes steps proportional to height of heap in worst case to remove the root.

5) void insertElement()
          
	   O(height)     height = logn if balanced heap |||between logn -> n in general

           complexity as takes steps proportional to height of heap in worst case to insert a new element.


-------------------------------------------------------------------------------------------------------------------------------------
