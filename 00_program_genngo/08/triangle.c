#include <stdio.h>
#include "renzoku.h"

int main(void)
{
    int number;
    printf("何列表示しますか？");
    scanf("%d", &number);
    for (int y = 0; y < number + 1; y++)
    {
        renzoku(y);
        printf("\n");
    }
}