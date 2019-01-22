#include<iostream>
#include<fstream>
#include<string.h>
#include<algorithm>
#include<iomanip>

using namespace std;

// DNA SEQUENCE ALIGNMENT ALGORITHM - USING DYNAMIC PROGRAMMING

// Declaring algorithm function to be used
void DNASequenceAlignment(string sequence1, string sequence2);

int main(void)
{
    // Prompting user to enter the input strings and storing them inside strings
    string sequence1, sequence2;
    cout<<"\nEnter first sequence (A, T, G, C)  : ";
    cin>>sequence1;
    cout<<"\nEnter second sequence (A, T, G, C) : ";
    cin>>sequence2;

    // Calling DNA sequence algorithm on the two strings
    DNASequenceAlignment(sequence1, sequence2);

    return 0;
}

void DNASequenceAlignment(string sequence1, string sequence2)
{
    // Initializing penalties
    int sameLetterPenalty = 0;
    int mismatchPenalty = 1;
    int gapMatchingPenalty = 2;

    // Declaring the dp matrix with its appropriate size, 1 column/row
    // for empty string (#) and rest for the rest of the letters of the string
    int m = sequence1.length() + 1;
    int n = sequence2.length() + 1;
    int dpMatrix[m][n];

    //Filling out values in the dp matrix
    for(int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            // Adding scores of corresponding according to penalties with the
            // empty string and the top row and leftmost column denote empty strings
            // penalty is i * 2 for leftmost column and j * 2 for top row, but
            // (i + j) * 2 works as one is zero when other isn't. Base case
            if(i == 0 or j == 0)
            {
                dpMatrix[i][j] = (i + j) * 2;
            }
            // Real algorithm step. Above step was kind of a base case
            else
            {
                // Three possible alignments to choose from (in actual 4 but its redundant)
                int option1, option2, option3;
                // If the current corresponding letters are the same
                if(sequence1[i - 1] == sequence2[j - 1])
                {
                    // Matching ith character with jth character + no penalty(because same letter)
                    option1 = dpMatrix[i - 1][j - 1] + sameLetterPenalty;

                    // Matching ith character with an empty gap ' '
                    option2 = dpMatrix[i - 1][j] + gapMatchingPenalty;

                    // Matching jth character with an empty gap
                    option3 = dpMatrix[i][j - 1] + gapMatchingPenalty;

                    // Storing minimum of the three possibilities
                    dpMatrix[i][j] = min(option1, min(option2, option3));
                }
                // Else if the current corresponding characters are different
                else if (sequence1[i - 1] != sequence2[j - 1])
                {
                  // Matching ith character with jth character + penalty of mismatch
                  option1 = dpMatrix[i - 1][j - 1] + mismatchPenalty;

                  // Matching ith character with an empty gap
                  option2 = dpMatrix[i - 1][j] + gapMatchingPenalty;

                  // Matching jth character with an empty gap
                  option3 = dpMatrix[i][j - 1] + gapMatchingPenalty;

                  // Storing minimum of the three possibilities
                  dpMatrix[i][j] = min(option1, min(option2, option3));
                }
            }
        }

    }

    // Printing the dp matrix
    cout << endl;
    cout << "The Dynamic Programming Matrix is as follows : \n";
    for(int i = 0; i < m ; i++ )
    {

        // Printing second sequence as top heading
        if(i == 0)
        {
            cout << endl << " " << setw (10) << "#";
            for(int k = 0; k < n; k++)
            {
                cout << setw(10) << sequence2[k];
            }
            cout << endl << endl << "#";
        }

        // Printing first sequence as leftmost vertical heading character by
        // character alongwith dp matrix values in the corresponding rows
        if(i != 0)
        {
            cout << sequence1[i - 1];

        }
        for(int j = 0; j < n ; j++)
        {
            cout << setw(10) << dpMatrix[i][j];
        }
        cout << endl;
    }
    cout << endl;


    // Backtracking to get the best possible alignment in string format also
    //Starting from the bottom left corner of dp matrix with corresponding whole strings
    int i = m - 1,j = n - 1;

    // Respective strings to store the best alignments
    string seq1, seq2;

    // Backtracking
    while(i > 0 && j > 0)
    {
        // Three possible alignments to choose from (in actual 4 but its redundant)
        int option1, option2, option3;

        // If the current corresponding letters are the same
        if (sequence1[i - 1] == sequence2[j - 1])
        {
            // Computing which case was used to get the optimal answer
            option1 = dpMatrix[i - 1][j - 1] + sameLetterPenalty;
            option2 = dpMatrix[i - 1][j] + gapMatchingPenalty;
            option3 = dpMatrix[i][j - 1] + gapMatchingPenalty;

            // Using the appropriate case to store the best possible alignment
            // Storing strings backwards (will reverse at the end)
            // # denotes gap

            if (dpMatrix[i][j] == option1)
            {
                seq1.push_back(sequence1[i - 1]);
                seq2.push_back(sequence2[j - 1]);
                i--;
                j--;

            }
            else if (dpMatrix[i][j] == option2)
            {
                seq1.push_back(sequence1[i - 1]);
                seq2.push_back('#');
                i--;
            }
            else if (dpMatrix[i][j] == option3)
            {
                seq1.push_back('#');
                seq2.push_back(sequence2[j - 1]);
                j--;
            }

        }

        // Else if the current corresponding letters are different
        else if (sequence1[i - 1] != sequence2[j - 1])
        {
            // Computing which case was used to get the optimal answer
            option1 = dpMatrix[i - 1][j - 1] + mismatchPenalty;
            option2 = dpMatrix[i - 1][j] + gapMatchingPenalty;
            option3 = dpMatrix[i][j - 1] + gapMatchingPenalty;

            // Using the appropriate case to store the best possible alignment
            // Storing strings backwards (will reverse at the end)
            // # denotes gap
            if (dpMatrix[i][j] == option1)
            {
                seq1.push_back(sequence1[i - 1]);
                seq2.push_back(sequence2[j - 1]);
                i--;
                j--;

            }
            else if (dpMatrix[i][j] == option2)
            {
                seq1.push_back(sequence1[i - 1]);
                seq2.push_back('#');
                i--;
            }
            else if (dpMatrix[i][j] == option3)
            {
                seq1.push_back('#');
                seq2.push_back(sequence2[j - 1]);
                j--;
            }

        }
    }

    // Matching gap (#) with the left out elements
    while (i > 0)
    {
        seq1.push_back(sequence1[i - 1]);
        seq2.push_back('#');
        i--;
    }

    // Matching gap (#) with the left out elements
    while (j > 0)
    {
        seq1.push_back('#');
        seq2.push_back(sequence2[j - 1]);
        j--;
    }

    // Reversing the alignments because they were stored in the reverse order
    reverse(seq1.begin(), seq1.end());
    reverse(seq2.begin(), seq2.end());

    // Printing the results
    cout << "\n\nThe best alignment of the two sequences is :\n\n";
    cout << "\n\nFIRST STRING  :" << seq1;
    cout << "\nSECOND STRING :" << seq2 << endl;
    cout << "The best possible alignment has cost : " << dpMatrix[m - 1][n - 1] << endl;
}
