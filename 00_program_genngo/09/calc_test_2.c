#include <stdio.h>
#include "calc/calc.h"
#include "renzoku/renzoku.h"

int main()
{
    int num1, num2;

    printf("num1を入力してください: ");
    scanf("%d", &num1);
    printf("num1の値は %d です\n", num1);

    printf("num2を入力してください: ");
    scanf("%d", &num2);
    printf("num2の値は %d です\n", num2);

    int num = add(num1, num2);
    for (int i = 0; i < num; i++)
    {
        printf("GQ");
        renzokuc(i, 'u');
        printf("X");
        printf("\n");
    }
    return 0;
}