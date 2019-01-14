#include <stdio.h>
#include <stdlib.h>

// MERGE SORT

// Declaring functions required
void mergeSort(int arr[], int low, int high);
void merge(int arr[], int low, int mid, int high);

// Declaring a variable to keep track of the number of inversions
unsigned long long int noOfInversions = 0;

int main()
{
    // Reading input elements from the file and storing inside an array
    FILE* inptr = fopen("IntegerArray.txt", "r");
    int arr[100000];
    int x;
    int i;
    char line[100];
    for (i = 0; i < 100000; i++)
    {
        fgets(line, sizeof(line), inptr);
        arr[i] = atoi(line);

    }
    fclose(inptr);

    // Printing input array
    printf("\nThe input array is as follows : \n\n");
    for (i = 0; i < 100000; i++)
    {
        printf("%d \t ", arr[i]);
    }

    // Calling merge sort algorithm on array
    mergeSort(arr, 0, 99999);

    // Printing final sorted array
    printf("\n\nThe sorted array is as follows : \n\n");
    for (i = 0; i < 100000; i++)
    {
        printf("%d \t ", arr[i]);
    }

    // Printing the number of inversions encountered in the array
    printf("\nThe number of inversions in this array is :  %lld \n", noOfInversions);

}


void mergeSort(int arr[], int low, int high)
{
    // Recursion case
	  if (low < high)
	  {
        // calling merge sort on the two halves of the array and then merging them
	      int mid = (low + high) / 2;
		    mergeSort(arr, low, mid);
	      mergeSort(arr, mid + 1, high);
	      merge(arr, low, mid, high);
    }
    // Base case
    else
    {
        return;
    }
}


void merge(int arr[],int low,int mid,int high)
{
    // Declaring two copies of the halves of the array on which merging is to be done
	  int arr1[50000];
	  int arr2[50000];
	  int n1 = mid - low + 1;
	  int n2 = high - mid;
	  int i, j, k;
	  for(i = 0; i < n1; i++)
    {
	      arr1[i] = arr[low + i];
    }
    for(i = 0; i < n2; i++)
    {
	    arr2[i] = arr[mid + 1 + i];
    }
    i = j = 0;

    // Merging the two halves (copies)
	  k = low;
    while(i < n1 && j < n2 && k <= high)
    {
    	  if(arr2[j] <= arr1[i])
    	  {
    		    arr[k] = arr2[j];
    		    j++;
    		    k++;
            // Incrementing number of inversions
    		    noOfInversions += (n1 - i);
		    }
		    else
		    {
			      arr[k] = arr1[i];
			      i++;
			      k++;
		    }
	  }

    // Appending to the result the left out elements of right half
	  if(i == n1 && j < n2)
	  {
		    while(j < n2 && k <= high)
		    {
			      arr[k] = arr2[j];
			      j++;
			      k++;
		    }
	  }

    // Appending to the result the left out elements of the left half
	  else if (i < n1 && j == n2)
	  {
		    while(i < n1 && k <= high)
		    {
			      arr[k] = arr1[i];
			      i++;
			      k++;
		    }
	  }

}
