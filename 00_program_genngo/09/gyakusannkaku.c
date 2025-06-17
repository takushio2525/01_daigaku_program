#include <stdio.h>
#include "renzoku/renzoku.h"

int main(void)
{
    int num = 10;
    for (int i = 0; i < num; i++)
    {

        renzokuc(num - i, ' ');
        renzokuc(i, '$');
        printf("\n");
    }
}