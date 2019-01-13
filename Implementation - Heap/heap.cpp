#include<iostream>
#include<fstream>

using namespace std;

void switchMenu();
class minHeap
{
    public:
      int arr[1000];
      int i1;
      int extractRoot(int heap[]);
      void printTop3Rows();
      void insertElement(int heap[],int element,int i);
      void removeRoot(int heap[],int i);
      minHeap()
      {
        i1 = 1;
        for(int i=0;i<1000;i++)
        {
            arr[i]=99999;
        }
      }


};

class maxHeap:public minHeap
{
    public:
      void insertElement(int heap[],int element,int i)
      {
          minHeap::insertElement(heap,-element,i);
      }
      void removeRoot(int heap[],int i)
      {
          minHeap::removeRoot(heap,i);
      }
      int extractRoot(int heap[])
      {
          return (-1)*(minHeap::extractRoot(heap));
      }
      void printTop3Rows();

};




int main(void)
{

    int element;
    int choice = 0;
    do
    {
        cout<<endl<<"Enter 1 for minHeap and 2 for maxHeap : ";
        cin>>choice;
    }
    while(!(choice!=1 || choice!=2));

    if(choice==1)
    {
        minHeap heap_1;
        choice=0;

        int noofelements;
        ifstream fin;
        fin.open("input.txt");
        if(!fin.is_open())
        {
            cout<<"COULD NOT OPEN THE FILE";
            return 0;
        }
        char noofelements_[15];
        fin>>noofelements_;
        noofelements=atoi(noofelements_);
        for (int i=0; i<noofelements; i++)
        {
            char element_[15];
            fin>>element_;
            element=atoi(element_);
            heap_1.insertElement(heap_1.arr,element,heap_1.i1);
        }
        fin.close();



        cout<<endl<<"THE INPUT.TXT IS SUCCESSFULLY INSERTED INTO THE HEAP";
        cout<<endl<<"PLEASE CHOOSE AMONG THE FOLLOWING OPERATIONS TO DO AS YOU LIKE";
        cout<<endl<<"___________________________________________________________________________________________________";
        do
        {
            cout<<endl<<"--------------------------------------------------------";
            cout<<endl<<"HEAP MENU ";
            cout<<endl<<"--------------------------------------------------------";
            cout<<endl<<"1. Insert an element into Heap ";
            cout<<endl<<"2. Delete root from Heap ";
            cout<<endl<<"3. Print the Heap top 3 rows";
            cout<<endl<<"4. Get the number of elements in the heap";
            cout<<endl<<"5. Get the value root of the heap";
            cout<<endl<<"0. Exit";
            cout<<endl<<"Enter a choice:  ";
            cin>>choice;
            cout<<endl<<"--------------------------------------------------------"<<endl;

            switch (choice)
            {
                case 1:
                    cout<<"Enter the element to insert into heap :  ";
                    cin>>element;
                    cout<<endl;
                    cout<<endl<<"--------------------------------------------------------"<<endl;
                    heap_1.insertElement(heap_1.arr,element,heap_1.i1);
                    cout<<endl;
                    cout<<"INSERTED!!";
                    break;

                case 2:
                    heap_1.removeRoot(heap_1.arr,1);
                    cout<<endl<<"REMOVED!!"<<endl;
                    break;
                case 3:
                    cout<<"TOP 3 ROWS OF HEAP: "<<endl;
                    heap_1.printTop3Rows();
                    cout<<endl;
                    break;
                case 4:
                    cout<<endl<<"The number of elements stored in the heap are: "<<heap_1.i1 - 1;
                    break;
                case 5:
                    cout<<endl;
                    cout<<"The root of the heap is: "<<heap_1.extractRoot(heap_1.arr);
                    cout<<endl;
                    break;

                case 0:
                    cout<<"BYE!!!";
                    break;

                default:
                    cout<<endl<<"YOU ENTERED AN INVALID CHOICE!!!";
                    break;

            }
        cout<<endl<<"___________________________________________________________________________________________________";
        }
        while (choice != 0);
        cout<<endl;

    }
    else
    {
        maxHeap heap_1;
        choice=0;

        int noofelements;
        ifstream fin;
        fin.open("input.txt");
        if(!fin.is_open())
        {
            cout<<"COULD NOT OPEN THE FILE";
            return 0;
        }
        char noofelements_[15];
        fin>>noofelements_;
        noofelements=atoi(noofelements_);
        for (int i=0; i<noofelements; i++)
        {
            char element_[15];
            fin>>element_;
            element=atoi(element_);
            heap_1.insertElement(heap_1.arr,element,heap_1.i1);
        }
        fin.close();




        cout<<endl<<"THE INPUT.TXT IS SUCCESSFULLY INSERTED INTO THE HEAP";
        cout<<endl<<"PLEASE CHOOSE AMONG THE FOLLOWING OPERATIONS TO DO AS YOU LIKE";
        cout<<endl<<"___________________________________________________________________________________________________";
        do
        {
            cout<<endl<<"--------------------------------------------------------";
            cout<<endl<<"HEAP MENU ";
            cout<<endl<<"--------------------------------------------------------";
            cout<<endl<<"1. Insert an element into Heap ";
            cout<<endl<<"2. Delete root from Heap ";
            cout<<endl<<"3. Print the Heap top 3 rows";
            cout<<endl<<"4. Get the number of elements in the heap";
            cout<<endl<<"5. Get the value root of the heap";
            cout<<endl<<"0. Exit";
            cout<<endl<<"Enter a choice:  ";
            cin>>choice;
            cout<<endl<<"--------------------------------------------------------"<<endl;

            switch (choice)
            {
                case 1:
                    cout<<"Enter the element to insert into heap :  ";
                    cin>>element;
                    cout<<endl;
                    cout<<endl<<"--------------------------------------------------------"<<endl;
                    heap_1.insertElement(heap_1.arr,element,heap_1.i1);
                    cout<<endl;
                    cout<<"INSERTED!!";
                    break;

                case 2:
                    heap_1.removeRoot(heap_1.arr,1);
                    cout<<endl<<"REMOVED!!"<<endl;
                    break;
                case 3:
                    cout<<"TOP 3 ROWS OF HEAP: "<<endl;
                    heap_1.printTop3Rows();
                    cout<<endl;
                    break;
                case 4:
                    cout<<endl<<"The number of elements stored in the heap are: "<<heap_1.i1 - 1;
                    break;
                case 5:
                    cout<<endl;
                    cout<<"The root of the heap is: "<<heap_1.extractRoot(heap_1.arr);
                    cout<<endl;
                    break;

                case 0:
                    cout<<"BYE!!!";
                    break;

                default:
                    cout<<endl<<"YOU ENTERED AN INVALID CHOICE!!!";
                    break;

            }
        cout<<endl<<"___________________________________________________________________________________________________";
        }
        while (choice != 0);
        cout<<endl;
    }
    return 0;



}

int minHeap::extractRoot(int heap[])
{
    return heap[1];
}


void minHeap::insertElement(int heap[],int element,int i)
{
    int parenti;
    heap[i]=element;
    parenti=i/2;

    if(parenti!=0 && heap[i]<heap[parenti])
    {
        int temp;
        temp=heap[parenti];
        heap[parenti]=heap[i];
        heap[i]=temp;
        insertElement(heap,element,parenti);
    }
    else
    {
        i1+=1;
        return;
    }


}

void minHeap::removeRoot(int heap[],int i)
{
    if (heap[i]==99999)
    {
        i1-=1;
        return;
    }
    int child1= 2 * i;
    int child2= (2 * i) + 1;
    if (heap[child1]==99999 && heap[child2]==99999)
    {
        heap[i]=99999;
        i1-=1;
        return;
    }
    else if(heap[child2]==99999)
    {
        int temp = heap[i];
        heap[i] = heap[child1];
        heap[child1]=99999;
        i1-=1;
        return;
    }
    else if (heap[child1]==99999)
    {
        int temp = heap[i];
        heap[i] = heap[child2];
        heap[child2]=99999;
        i1-=1;
        return;
    }

    if (heap[child1]<= heap[child2])
    {
        int temp=heap[i];
        heap[i]=heap[child1];
        heap[child1]=temp;
        removeRoot(heap,child1);
    }
    else
    {
        int temp=heap[i];
        heap[i]=heap[child2];
        heap[child2]=temp;
        removeRoot(heap,child2);
    }

}
void minHeap::printTop3Rows()
{
    cout<<endl;
    cout<<arr[1];
    cout<<endl;
    cout<<arr[2]<<"  "<<arr[3];
    cout<<endl;
    cout<<arr[4]<<"  "<<arr[5]<<"  "<<arr[6]<<"  "<<arr[7];
}

void maxHeap::printTop3Rows()
{
    cout<<endl;
    cout<<-arr[1];
    cout<<endl;
    cout<<-arr[2]<<"  "<<-arr[3];
    cout<<endl;
    cout<<-arr[4]<<"  "<<-arr[5]<<"  "<<-arr[6]<<"  "<<-arr[7];
}
