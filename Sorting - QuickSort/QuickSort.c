#include <stdio.h>
#include <stdlib.h>


void quickSort(int arr[], int low, int high);
unsigned long int noOfSwaps = 0;

int main()
{

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

	printf("\nThe original array looks as follows : \n\n");
	for(i = 0; i < 10000; i++)
	{
		printf("%d  \t", arr[i]);
	}
	quickSort(arr, 0, 9999);

	printf("\n\nThe sorted array looks as follows : \n\n");
	for(i = 0; i < 10000; i++)
	{
		printf("%d  \t", arr[i]);
	}

	printf("\n\nThe number of swaps is :  %ld \n\n", noOfSwaps);

}


void quickSort(int arr[], int low, int high)
{
		if(low >= high)
		{
				return;
		}

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
		// Computing privot as the median of the start, middle and end elements of the array/subarray in concern
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
    temp = arr[low];
    arr[low] = pivot;
    arr[pivotPosition] = temp;

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

		noOfSwaps += high - low;
		quickSort(arr, low, i - 2);
		quickSort(arr, i, high);

}
