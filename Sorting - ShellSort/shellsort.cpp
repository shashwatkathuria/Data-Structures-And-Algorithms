#include<iostream>
#include<fstream>
using namespace std;

// SHELL SORT ALGORITHM

// Declaring function required for sorting
void shellSort(long int arr[], long int noOfElements);


int main(void)
{
    // Opening file to be read
    ifstream fin;
    long int noOfElements;
    fin.open("IntegerArray.txt");
    if( !fin.is_open() )
    {
        cout << "COULD NOT OPEN THE FILE";
        return 0;
    }

    // Reading input number of elements and initializing variables required
    long int number;
    char noOfElements_[15];

    fin >> noOfElements_;
    noOfElements = atoi(noOfElements_);
    long int arr[noOfElements];

    // Printing input elements and storing each element inside an array
    cout << "\n\n The input linked list is as follows : \n\n";
    for (long int i = 0; i < noOfElements; i++)
    {
        char number_[15];
        fin >> number_;
        number = atoi(number_);
        cout << number << "\t";
        arr[i] = number;
    }
    cout<<"\n\n";

    //Calling shell sort algorithm on the array
    shellSort(arr, noOfElements);
}

void shellSort(long int arr[], long int noOfElements)
{
    // Initializing variable to keep track of number of swaps
    long int noOfSwaps = 0;

    // For loop for insertion sort for each gap elements array
    for(long int gap = noOfElements / 2; gap >= 1; gap /= 2)
    {
        // Printing gap info
        cout << "COMPUTING ON GAP : " << gap << endl;

        // Insertion sort on gap elements apart subarrays
        for(long int i = gap; i < noOfElements; i += 1)
        {

            // Storing element and position to be inserted into left sorted part of subarray
            long int element = arr[i];
            long int pos = i;

            // Bubbling concerned elements right to make space to insert the
            // required element into its correct position
            while(pos != 0 && pos - gap >= 0 && arr[pos - gap] > element )
            {
              noOfSwaps += 1;
              arr[pos] = arr[pos - gap];
              pos -= gap;
            }

            // Inserting the required element into its correct position
            arr[pos] = element;

        }
    }

    // Printing sorted array
    cout<<"\n\nThe sorted array looks as follows : \n\n";
    for(long int i = 0; i < noOfElements; i++)
    {
      cout << arr[i] << "\t";
    }

    // Printing number of swaps encountered
    cout << endl << endl << "The number of swaps encountered is : " << noOfSwaps << endl << endl;
    return;
}
