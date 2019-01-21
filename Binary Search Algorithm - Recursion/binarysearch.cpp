#include<iostream>
#include<fstream>
using namespace std;

void binarySearch(int arr[], int low, int high, int elementToBeSearched);
int main(void)
{
    ifstream fin;
    fin.open("SortedArray.txt");
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

    int elementToBeSearched;
    cout << "\nEnter the element which you want to search for : ";
    cin >> elementToBeSearched;
    binarySearch(arr, 0, noOfElements,elementToBeSearched);


}

void binarySearch(int arr[], int low, int high, int elementToBeSearched)
{
    if (low > high)
    {
        cout << "\nElement not present in the array.\n";
        return;
    }
    else
    {
        int mid = (low + high) / 2;
        if (arr[mid] == elementToBeSearched)
        {
            cout << "\nElement present at position : " << ( mid + 1 ) << "\n";
            return;
        }
        else
        {
            if(elementToBeSearched < arr[mid])
            {
                binarySearch(arr, low, mid - 1, elementToBeSearched);
            }
            else
            {
                binarySearch(arr, mid + 1, high, elementToBeSearched);
            }
        }
    }
}
