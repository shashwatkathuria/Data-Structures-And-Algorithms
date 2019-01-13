_____________________
SHASHWAT KATHURIA
B17CS050
CSE BRANCH
ASSIGNMENT 5
_____________________

TRIE
_____________________
------------------------------------
INSTRUCTIONS TO RUN THE PROGRAM
------------------------------------
1. Run ./a.out in the terminal to run the program and get the output.

2. The entries in the file "input.txt" which are randomly generated are inserted
   into the trie once the program starts running after the user is prompted for
   the number of words to generate randomly.

----------------
OUTPUT
----------------
--)  "output.txt" contains the output of "trie.cpp".
_______________________________________________________________________________________
------------------------------------
COMPONENTS OF THE FILE
------------------------------------

--) || g++ trie.cpp ||

    1.  "input.txt" file contains random string entries with the number of such entries being
         the number specified by the user in the starting of the program.

    2. "./a.out" contains the compiled file compiled using g++ compiler.

    3. "trie.cpp" is the program written in C++.

    4. "output.txt" contains the output of the program.


-----------------------------------
TIME COMPLEXITIES
------------------------------------

class Trie

1) Trie()

          O(1)

          complexity because initializing the two data members takes constant
          number of steps.

2) bool searchWord(const char *word)

          O(length of word)

          complexity as takes n number of steps to go deeper inside the trie in order
          to find the given word in the worst case.

3) bool load()
          O(m * n)        [ where m=number of words to be inserted ]
                          [ where n=maximum length of a word       ]
          complexity as the maximum length of a word is n letters  so in the worst case
          the time taken is n multiplied by m number of words and for each word the number of steps
          taken is equal to the length of the word so it follows that the complexity would be m * n.

4) unsigned int size()
          O(1)

          complexity as takes constant number of steps to return the number of words in trie.

5) bool unload()
          O(m * n)        [ where m=number of words to be inserted ]
                          [ where n=maximum length of a word       ]
          complexity as the maximum length of a word is n letters  so in the worst case
          the time taken is n multiplied by m number of words and for each word the number of steps
          taken is equal to the length of the word so it follows that the complexity would be m * n.

6) bool insertNewWord()
          O(length of word)

          complexity as takes n number of steps to go deeper inside the trie in order
          to insert the given word as well as check in the initial step whether the word
          was already in the trie or not.

7)bool deleteWord()
          O(length of word)

          complexity as takes n number of steps to go deeper inside the trie in order
          to delete the given word in the worst case(if the word was present in the trie).

8)void freeNode(node *currentNode)
          O(m * n)        [ where m=number of words to be inserted ]
                          [ where n=maximum length of a word       ]
          complexity as recursively calls itself until all the nodes in the trie are
          successfully deleted and freed which is equal to m * n.

9)bool randomInputGenerator()
          O(m * n)        [ where m=number of words to be inserted ]
                          [ where n=maximum length of a word       ]
          complexity as randomly generates m number of words whose maximum length is n
          so it follows that the time complexity will be m * n.

----------------------------------X--------------------------------------X-------------------------------------------------------------
