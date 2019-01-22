#include<iostream>
#include<fstream>
#include<string.h>
#include<algorithm>
#include<iomanip>

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
    return 0;
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

    cout << endl;
    cout<<"The Dynamic Programming Matrix is as follows : \n";
    for(int i = 0; i < m ; i++ )
    {

        if(i == 0)
        {
            cout << endl <<" "<<setw (10)<< "#";
            for(int k = 0; k < n; k++)
            {
                cout << setw(10) << sequence2[k];
            }
            cout <<endl<< endl << "#";
        }

        if(i != 0)
        {
            cout <<sequence1[i - 1];

          }
        for(int j = 0; j < n ; j++)
        {
            cout << setw(10) << dpMatrix[i][j];
        }
        cout << endl;
    }
    cout << endl;



    int i = m - 1,j = n - 1;
    string seq1,seq2;
    while(i > 0 && j > 0)
    {
        int option1,option2,option3;
        if(sequence1[i - 1] == sequence2[j - 1])
        {
            option1 = dpMatrix[i - 1][j - 1] + 0;
            option2 = dpMatrix[i - 1][j] + 2;
            option3 = dpMatrix[i][j - 1] + 2;
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
        else if (sequence1[i - 1] != sequence2[j - 1])
        {
            option1 = dpMatrix[i - 1][j - 1] + 1;
            option2 = dpMatrix[i - 1][j] + 2;
            option3 = dpMatrix[i][j - 1] + 2;
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
    while(j > 0)
    {
        seq2.push_back(sequence2[j - 1]);
        seq1.push_back('#');
        j--;
    }
    while(i > 0)
    {
        seq1.push_back(sequence1[i - 1]);
        seq2.push_back('#');
        i--;
    }

    reverse(seq1.begin(), seq1.end());
    reverse(seq2.begin(), seq2.end());
    cout<<"\n\nThe best alignment of the two sequences is :\n\n";
    cout<<"\n\nFIRST STRING  :"<<seq1;
    cout<<"\nSECOND STRING :"<<seq2<<endl;
}
