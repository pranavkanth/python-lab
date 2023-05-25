#include<stdio.h>

int main()
{
    int a[5] = {5, 3, 1, 2, 4, 8, 6, 7, 9, 10};
    
    for(int i = 0; i < 5; i++)
    {
        for(int j = 0; j < i + 1; j++)
        {
            if(a[i] < a[j])
            {
                int temp = a[i];
                a[i] = a[j];
                a[j] = temp;
            }
        }
    }
    
    for(int i = 0; i < 5; i++)
    {
        printf("%d", a[i]);
    }

    return 0;
}