#include <stdio.h>
#include <stdlib.h>

// QUICK SORT

// Declaring the function required
void quickSort(int arr[], int low, int high);

// Declaring a variable to keep track of the number of swaps made during sorting
unsigned long int noOfSwaps = 0;

int main()
{

		// Reading elements from the input file and storing them in an array
		FILE* inptr = fopen("QuickSort.txt", "r");
		char line[100];
		int arr[10000];
		int i = 0;
		for(i = 0; i < 10000; i++)
		{
		    fgets(line, sizeof(line), inptr);
				arr[i] = atoi(line);
		}
		fclose(inptr);

		// Printing the original array
		printf("\nThe original array looks as follows : \n\n");
		for(i = 0; i < 10000; i++)
		{
			printf("%d  \t", arr[i]);
		}

		// Calling the quick sort algorithm on the array
		quickSort(arr, 0, 9999);

		// Printing the sorted array
		printf("\n\nThe sorted array looks as follows : \n\n");
		for(i = 0; i < 10000; i++)
		{
			printf("%d  \t", arr[i]);
		}

		// Printing the number of swaps encountered
		printf("\n\nThe number of swaps is :  %ld \n\n", noOfSwaps);

}


void quickSort(int arr[], int low, int high)
{
		// Base case
		if(low >= high)
		{
				return;
		}

		// Computing positions of start, middle and end in the array/subarray
    int mid;
    int temp;
    int noOfElements = high - low + 1;
    if ( ( noOfElements / 2 ) * 2 == noOfElements )
		{
        mid = noOfElements / 2 - 1;
		}
		else
		{
        mid = noOfElements / 2;
		}

		int pivot;
    int pivotPosition;

		// Computing pivot as the median of the start, middle and end elements of the array/subarray in concern
    if( (arr[mid] < arr[low] && arr[high] > arr[low]) || (arr[mid] > arr[low] && arr[high] < arr[low]) )
    {
        pivot = arr[low];
        pivotPosition = low;
    }
    else if ( (arr[low] < arr[mid] && arr[high] > arr[mid]) || (arr[low] > arr[mid] && arr[high] < arr[mid]) )
    {
				pivot = arr[mid];
				pivotPosition = mid;
    }
		else
		{
         pivot = arr[high];
         pivotPosition = high;
    }
		// Swapping the pivot with the first element in the array/subarray
    temp = arr[low];
    arr[low] = pivot;
    arr[pivotPosition] = temp;

		// Swapping elements to put the pivot in its correct position,
		// by putting smaller elements to the left and bigger to the right
		int i = low + 1, j = low + 1;
		for(j = low + 1; j <= high; j++)
		{
				if(pivot > arr[j])
				{
						temp = arr[i];
						arr[i] = arr[j];;
						arr[j] = temp;
						i++;
				}

		}
		temp = arr[i - 1];
		arr[i - 1] = pivot;
		arr[low] = temp;

		// Incrementing number of swaps
		noOfSwaps += high - low;
		
		// Calling quick sort recursively on the two subarrays, not including the pivot
		quickSort(arr, low, i - 2);
		quickSort(arr, i, high);

}
