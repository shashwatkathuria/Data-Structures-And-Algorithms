#include<iostream>
#include<fstream>
using namespace std;

// Declaring function required to do binary search
void binarySearch(int arr[], int low, int high, int elementToBeSearched);

int main(void)
{

    // Reading inputs from input file and storing inside an array
    ifstream fin;
    fin.open("SortedArray.txt");

    // Terminating if input file cannot be opened
    if(!fin.is_open())
    {
        cout << "\nCOULD NOT OPEN THE FILE\n";
        return 0;
    }
    char noOfElements_[15];
    fin >> noOfElements_;
    int noOfElements = atoi(noOfElements_);

    int arr[noOfElements];
    for(int i = 0;i < noOfElements;i++)
    {
        char element[15];
        fin >> element;
        arr[i] = atoi(element);
    }

    // Prompting user for the element to be searched in the sorted array
    int elementToBeSearched;
    cout << "\nEnter the element which you want to search for : ";
    cin >> elementToBeSearched;

    // Calling binary search algorithm on the array
    binarySearch(arr, 0, noOfElements,elementToBeSearched);


}

// Function to perform binary search on a sorted array given a element to be searched for in the array
void binarySearch(int arr[], int low, int high, int elementToBeSearched)
{
    // Base case
    // Returning if the element is not found
    if (low > high)
    {
        cout << "\nElement not present in the array.\n";
        return;
    }
    else
    {
        // Determining the middle index to split the array into two parts
        int mid = (low + high) / 2;

        // Returning the middle element if it is the element being searched
        if (arr[mid] == elementToBeSearched)
        {
            cout << "\nElement present at position : " << ( mid + 1 ) << "\n";
            return;
        }

        // Otherwise recursively calling on the appropriate half of the array
        else
        {
            // Calling on the left half if the middle element is bigger
            if(elementToBeSearched < arr[mid])
            {
                binarySearch(arr, low, mid - 1, elementToBeSearched);
            }

            // Calling on the right half if the middle element is smaller
            else
            {
                binarySearch(arr, mid + 1, high, elementToBeSearched);
            }
        }
    }
}
