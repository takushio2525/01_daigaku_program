#include <stdio.h>

int main()
{
    printf("\n");

    for (int i = 0; i < 9; i++)
    {
        for (int j = 0; j < i + 1; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}