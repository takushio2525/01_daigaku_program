#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//頭の体操

#define ARR_SIZE 6

int mymax(int *arr, int size);
int max_index(int *arr, int start, int size);
void max_order(int *arr, int size);

int main()
{
    srand((unsigned int)time(NULL));

    int A[ARR_SIZE];

    for (int i = 0; i < ARR_SIZE; i++)
    {

        A[i] = (rand() % 100) + 1;
    }
    printf("A=");
    for (int i = 0; i < ARR_SIZE; i++)
    {
        printf("%d ", A[i]);
    }
    printf("\n");

    printf("%d\n", mymax(A, ARR_SIZE));
    printf("%d\n", max_index(A, 0, ARR_SIZE));

    max_order(A, ARR_SIZE);
    for (int i = 0; i < ARR_SIZE; i++)
    {
        printf("%d ", A[i]);
    }

    return 0;
}

int mymax(int *arr, int size)
{
    int max = arr[0];

    for (int i = 0; i < size; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
        }
    }
    return max;
}

int max_index(int *arr, int start, int size)
{
    int max = arr[start];
    int maxIndex = start;

    for (int i = start; i < size; i++)
    {
        if (max < arr[i])
        {
            max = arr[i];
            maxIndex = i;
        }
    }
    return maxIndex;
}

void max_order(int *arr, int size)
{
    for (int i = 0; i < size; i++)
    {

        int ind = max_index(arr, i, size);
        if (ind != i)
        {
            int buff = arr[i];
            arr[i] = arr[ind];
            arr[ind] = buff;
        }
    }
}
