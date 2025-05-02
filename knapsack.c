#include<stdio.h>
int max(int a,int b)
{
    if(a>b)
    return(a);
    else 
    return(b);
}
int knapsack(int W,int val[],int wt[],int n)
{
    int i,w;
    int k[n+1][W+1];
    for(i=0;i<=n;i++)
    {
        for(w=0;w<=W;w++)
        {
            if(i==0||w==0)
            {
                k[i][w]=0;
            }
            else if(wt[i-1]<=w)
            {
                k[i][w]=max(val[i-1]+k[i-1][w-wt[i-1]],k[i-1][w]);
            }
            else
            {
                k[i][w]=k[i-1][w];
            }
        }
    }
    return k[n][W];
}
int main()
{
    int val[100],wt[100],W,n,i;
    printf("Enter the number of elements:");
    scanf("%d",&n);
    for(i=0;i<n;i++)
    {
        printf("Enter the weight and value of item %d: ",i+1);
        scanf("%d %d",&wt[i],&val[i]);
    }
    printf("Enter the maximum weight that can be drawn:");
    scanf("%d",&W); 
    printf("The maximum value can be withdrawn is: %d",knapsack(W,val,wt,n));
}