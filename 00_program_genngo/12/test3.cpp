#include <stdio.h>

int main()
{
    int x[] = {1, 2, 3};
    int *y;

    printf("%d, %d, %d\n", x[0], x[1], x[2]);

    y = x;
    printf("%d, %d, %d\n", y[0], y[1], y[2]);

    y[1] = 5;
    printf("%d, %d, %d\n", x[0], x[1], x[2]);

    return 0;
}