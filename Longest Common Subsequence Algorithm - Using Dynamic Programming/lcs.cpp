#include<iostream>
#include<string.h>
//algorithm library used to reverse a string
#include<algorithm>

// LONGEST COMMON SUBSEQUENCE ALGORITHM - USING DYNAMIC PROGRAMMING

using namespace std;
//Declaring the longest common sequence algorithm function
void longestCommonSubsequence(string s1,string s2);

int main(void)
{
    string s1,s2;

    //Taking input for first string
    cout << "Enter first string  :  ";
    cin >> s1;
    cout << endl;

    //Taking input for second string
    cout << "Enter second string :  ";
    cin >> s2;
    cout << endl;

    //Passing strings into function
    longestCommonSubsequence(s1, s2);

}

void longestCommonSubsequence(string s1, string s2)
{

    string longestSubsequence;

    //Obtaining the lengths of the two strings
    int s1Length = s1.length() , s2Length = s2.length();

    //Declaring matrix for storing the dynamic programming subproblems answers
    int dpMatrix[ s1Length + 1 ][ s2Length + 1 ];

    //Filling dpMatrix
    for(int i = 0 ;i <= s1Length ; i++)
    {
        for(int j = 0; j <= s2Length ; j++)
        {
            //Filling zeros in first column and first row because of comparison with an empty string
            if(i == 0 || j == 0)
            {
                  dpMatrix[i][j] = 0;
            }
            //Filling out remaining cells according to dynamic approach
            else
            {
                  //If same letters found , diagonally incrementing the cell by 1
                  if(s1[i -  1] == s2 [j - 1])
                  {
                      dpMatrix[i][j] = dpMatrix[i - 1][j - 1] + 1;
                  }

                  //If different letters found , putting maximum of upper and left adjacent column
                  else
                  {
                      dpMatrix[i][j] = max(dpMatrix[i - 1][j] , dpMatrix[i][j - 1]);
                  }
            }

        }
    }
    //Printing the dpMatrix
    cout << endl;
    for(int i = 0; i <= s1Length ; i++ )
    {

        //Printing rows in required format
        if(i == 0)
        {
            //Printing string s2
            cout << endl << "   #";
            for(int k = 0; k < s2Length; k++)
            {
                cout << " " << s2[k];
            }
            cout << endl << "# ";
        }

        //Printing string s1 letter by letter
        if(i != 0)
        {
            cout << s1[i - 1] << " ";
        }

        //Printing columns in required format
        for(int j = 0; j <= s2Length ; j++)
        {
            cout << " " << dpMatrix[i][j];
        }
        cout << endl;
    }
    cout << endl;

    //Initiallizing variables for bactracking,starting from the rightmost bottom corner element
    int temp = dpMatrix[s1Length][s2Length];
    int itemp = s1Length, jtemp = s2Length;

    //Backtracking

    while(dpMatrix[itemp][jtemp] != 0)
    {

        //Concatenating answer to the string if corresponding elements of the two string are same
        if(s1[itemp - 1] == s2[jtemp - 1])
        {
            longestSubsequence += s1[itemp - 1];
            itemp--;
            jtemp--;

        }
        //Horizontally backtracking without concatenating if corresponding elements are not same
        else if (dpMatrix[itemp - 1 ][jtemp] > dpMatrix[itemp ][jtemp - 1]  )
        {
            itemp--;
        }
        //Vertically backtracking without concatenating if corresponding elements are not same
        else
        {
            jtemp--;
        }

    }

    //Reversing the string longestSubsequence to get answer in correct format
    reverse(longestSubsequence.begin(), longestSubsequence.end());

    //Printing results
    cout<<endl<<"The longest common subsequence has a length of : "<<dpMatrix[s1Length][s2Length]<<endl;
    cout<<endl<<"The longest common subsequence is : "<<longestSubsequence<<endl<<endl;
}
