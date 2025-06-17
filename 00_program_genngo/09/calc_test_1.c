#include <stdio.h>
#include "calc/calc.h"
int main()
{
    int num1, num2;

    printf("num1を入力してください: ");
    scanf("%d", &num1);
    printf("num1の値は %d です\n", num1);

    printf("num2を入力してください: ");
    scanf("%d", &num2);
    printf("num2の値は %d です\n", num2);


    printf("addテスト %d\n",add(num1, num2));
    printf("subテスト %d\n",sub(num1, num2));
    printf("mulテスト %d\n",mul(num1, num2));
    printf("divテスト %d\n",div(num1, num2));
    
    return 0;
}