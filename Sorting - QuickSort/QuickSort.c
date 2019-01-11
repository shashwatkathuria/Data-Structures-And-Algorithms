#include <stdio.h>
#include <stdlib.h>
unsigned long int ans=0;
void quickSort(int arr[], int low, int high);
int main(){
	
	FILE* inptr=fopen("QuickSort.txt","r");
	char line[100];
	int arr[10000];
	int i=0;
	for(i=0;i<10000;i++){
	    fgets(line,sizeof(line),inptr);
		arr[i]=atoi(line);
	}
	fclose(inptr);
	
	for(i=0;i<10000;i++)
	{
		printf("%d  \n",arr[i]);
	}
	quickSort(arr,0,9999);
	for(i=0;i<10000;i++)
	{
		printf("%d  \n",arr[i]);
	}
	printf("     %ld \n",ans);
}
void quickSort(int arr[],int low,int high)
{   
    if(low>=high)
     return;
    int mid;
    int temp;
    int n=high-low+1;
    if ((n/2)*2==n)
        mid=n/2-1;
    else
        mid=n/2;
    int pivot;
    int z;
    if((arr[mid]<arr[low] && arr[high]>arr[low])||(arr[mid]>arr[low] && arr[high]<arr[low]))
    {
         pivot=arr[low];
         z=low;
    }
    else if ((arr[low]<arr[mid] && arr[high]>arr[mid])||(arr[low]>arr[mid] && arr[high]<arr[mid]))
         {
		 pivot=arr[mid];
		 z=mid;
    }
	else
	{
         pivot=arr[high];
         z=high;
    }
    temp=arr[low];
    arr[low]=pivot;
    arr[z]=temp;
	int i=low+1,j=low+1;
	for(j=low+1;j<=high;j++)
	{
		if(pivot>arr[j]){
			temp=arr[i];
			arr[i]=arr[j];;
			arr[j]=temp;
			i++;
		}
		
	}
	temp=arr[i-1];
	arr[i-1]=pivot;
	arr[low]=temp;
	
	ans+=high-low;
	quickSort(arr,low,i-2);
	quickSort(arr,i,high);
	
	
}
