#include<stdio.h>
#include<limits.h>
#include<stdlib.h>
void swap(int *p,int *q)
{
    int temp;
    temp=*p;
    *p=*q;
    *q=temp;
}
int partition(int a[],int l,int h)
{
    int pivot,i,j;
    pivot=a[l];
    i=l;
    j=h;
    do
    {
        do
        {
            i++;
        }while (a[i]<=pivot);
        do
        {
            j--;
        }while (a[j]>pivot);
        if(i<j)
        {swap(&a[i],&a[j]);}

    } while (i<j);
swap(&a[l],&a[j]);
return j;
}
void quicksort(int a[],int l,int h)
{
 int j;
 if(l<h)
 {
    j=partition(a,l,h);
    quicksort(a,l,j);
    quicksort(a,j+1,h);
 }  
}
int main()
{
    int n,i;
    int *A;
    printf("Enter the size of array:\n");
    scanf("%d",&n);
    printf("Enter the array elements:\n");
    A = (int *)malloc((n + 1) * sizeof(int));
    for(i=0;i<n;i++)
    {
        scanf("%d",&A[i]);
    }
    A[n]=INT_MAX;
    quicksort(A,0,n);
    printf("Sorted elements are:\n");
    for(i=0;i<n;i++)
    {
        printf("%d ",A[i]);
    }
    return 0;
}