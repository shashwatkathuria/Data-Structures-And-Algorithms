#include<iostream>
#include<fstream>
using namespace std;

void shellSort(long int arr[], long int noOfElements);
int main(void)
{
    // Reading input elements from the file and storing inside a linked list
    ifstream fin;
    long int noOfElements;
    fin.open("IntegerArray.txt");
    if( !fin.is_open() )
    {
        cout << "COULD NOT OPEN THE FILE";
        return 0;
    }

    long int number;
    char noOfElements_[15];
    fin >> noOfElements_;
    noOfElements = atoi(noOfElements_);
    long int arr[noOfElements];

    // Printing input array
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

    shellSort(arr, noOfElements);
}

void shellSort(long int arr[], long int noOfElements)
{
    long int noOfSwaps = 0;
    for(long int gap = noOfElements / 2; gap >= 1; gap /= 2)
    {
      cout << "GAP IS : " << gap << endl;
      for(long int i = gap; i < noOfElements; i += gap)
      {

        long int element = arr[i];
        long int pos = i;

        while(pos != 0 && pos - gap >= 0 && arr[pos - gap] > element )
        {
          noOfSwaps += 1;
          arr[pos] = arr[pos - gap];
          pos -= gap;
        }
        arr[pos] = element;

      }
    }

    for(long int i = 0;i<noOfElements;i++)
    {
      cout<<endl<<arr[i];
    }

    cout<<endl<<"The number of swaps : "<<noOfSwaps;
    return ;
}
