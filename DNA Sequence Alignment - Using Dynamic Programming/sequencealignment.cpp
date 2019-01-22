#include<iostream>
#include<fstream>
#include<string.h>

using namespace std;

void DNASequenceAlignment(string sequence1, string sequence2);
int main(void)
{
    string sequence1;
    string sequence2;
    cout<<"\nEnter first sequence : ";
    cin>>sequence1;
    cout<<"\nEnter second sequence : ";
    cin>>sequence2;
    DNASequenceAlignment(sequence1, sequence2);
}

void DNASequenceAlignment(string sequence1, string sequence2)
{
    int m = sequence1.length() + 1;
    int n = sequence2.length() + 1;
    int dpMatrix[m][n];
    for(int i = 0; i < m; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if(i == 0 or j == 0)
            {
                dpMatrix[i][j] = (i + j) * 2;
            }
            else
            {
                int option1,option2,option3;
                if(sequence1[i - 1] == sequence2[j - 1])
                {
                    option1 = dpMatrix[i - 1][j - 1] + 0;
                    option2 = dpMatrix[i - 1][j] + 2;
                    option3 = dpMatrix[i][j - 1] + 2;
                    dpMatrix[i][j] = min(option1,min(option2, option3));
                }
                else if (sequence1[i - 1] != sequence2[j - 1])
                {
                  option1 = dpMatrix[i - 1][j - 1] + 1;
                  option2 = dpMatrix[i - 1][j] + 2;
                  option3 = dpMatrix[i][j - 1] + 2;
                  dpMatrix[i][j] = min(option1, min(option2, option3));
                }
            }
        }
    }

    //Printing the dpMatrix
    cout << endl;
    for(int i = 0; i < m ; i++ )
    {

        //Printing rows in required format
        if(i == 0)
        {
            //Printing string s2
            cout << endl << "     #";
            for(int k = 0; k < n; k++)
            {
                cout << "  " << sequence2[k];
            }
            cout << endl << "#  ";
        }

        //Printing string s1 letter by letter
        if(i != 0)
        {
            cout << sequence1[i - 1] << "  ";

          }
        //Printing columns in required format
        for(int j = 0; j < n ; j++)
        {
            cout << "  " << dpMatrix[i][j];
        }
        cout << endl;
    }
    cout << endl;
}
