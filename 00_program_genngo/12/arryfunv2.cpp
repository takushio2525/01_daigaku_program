#include <stdio.h>

void address(int arr[]);

int main(void)
{
    int array[] = {97, 98, 99};
    printf("    array:%p\n", array);
    printf("&array[0]:%p\n", &array[0]);
    printf("&array[1]:%p\n", &array[1]);
    printf("&array[2]:%p\n", &array[2]);
    printf(" array[0]:%d\n", array[0]);
    printf(" array[1]:%d\n", array[2]);
    printf(" array[2]:%d\n", array[2]);
    address(array);
}

void address(int arr[])
{
    printf("    arr:%p\n", arr);
    printf("&arr[0]:%p\n", &arr[0]);
    printf("&arr[1]:%p\n", &arr[1]);
    printf("&arr[2]:%p\n", &arr[2]);
    printf(" arr[0]:%d\n", arr[0]);
    printf(" arr[1]:%d\n", arr[2]);
    printf(" arr[2]:%d\n", arr[2]);
}