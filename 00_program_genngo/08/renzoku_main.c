#include <stdio.h>
#include "renzoku.h"

int main(void)
{
    while (1)
    {
        int number;
        printf("何個表示しますか？");
        scanf("%d", &number);
        renzoku(number);
        printf("\n");
    }
}