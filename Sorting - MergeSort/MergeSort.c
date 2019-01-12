#include <stdio.h>
#include <stdlib.h>
unsigned int ans=0;
void merge_sort(int arr[],int low,int high);
void merge(int arr[],int low,int mid,int high);
int main()
{
  FILE* inptr=fopen("IntegerArray.txt","r");
    int arr[100000];
    int x;
    int i;
    char line[100];
    for (i=0;i<100000;i++)
    {
        fgets(line,sizeof(line),inptr);
        arr[i]=atoi(line);

    }
    fclose(inptr);
    for (i=0;i<100000;i++){
        printf("%d \n ",arr[i]);
        }
    merge_sort(arr,0,99999);
    for (i=0;i<100000;i++)
        printf("%d \n ",arr[i]);
        
    printf("\n   %lld \n",ans);
}

void merge_sort(int arr[],int low,int high){
	if (low<high)
	   {
	       int mid=(low+high)/2;
		   merge_sort(arr,low,mid);
	       merge_sort(arr,mid+1,high);
	       merge(arr,low,mid,high);
       }
}
void merge(int arr[],int low,int mid,int high){
	int arr1[50000];
	int arr2[50000];
	int n1=mid-low+1;
	int n2=high-mid;
	int i,j,k;
	for(i=0;i<n1;i++)
	    arr1[i]=arr[low+i];
	for(i=0;i<n2;i++)
	    arr2[i]=arr[mid+1+i];
	i=j=0;
	k=low;
    while(i<n1 && j<n2 && k<=high)
    {
    	if(arr2[j]<=arr1[i])
    	{
    		arr[k]=arr2[j];
    		j++;
    		k++;
    		ans+=(n1-i);
		}
		else
		{
			arr[k]=arr1[i];
			i++;
			k++;
		}
	}
	if(i==n1 && j<n2)
	{
		while(j<n2 && k<=high)
		{
			arr[k]=arr2[j];
			j++;
			k++;
		}
	}
	else if (i<n1 && j==n2)
	{
		while(i<n1 && k<=high)
		{
			arr[k]=arr1[i];
			i++;
			k++;
		}
	}

	
}


