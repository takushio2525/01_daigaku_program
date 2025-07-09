#include <stdio.h>

int main()
{
    int x[] = {1, 2, 3, 4, 50};
    int *a;

    a = x;
    printf("%p\n", x);
    printf("%p\n", a);

    printf("%d\n", *a);
    printf("%d\n", *(a + 1));
    printf("%d\n", *(a + 2));
    printf("%d\n", *(a + 3));
    printf("%d\n", *(a + 4));
}