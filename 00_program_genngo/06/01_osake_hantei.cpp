#include <stdio.h>

int main()
{
    int age;

    printf("年齢を入力してください\n");

    scanf("%d", &age);

    if(age>=18){
        printf("成人です\n");
    } else {
        printf("未成年です\n");
    }

    if (age >= 20)
    {
        printf("いっぱい飲んでください\n");
    }
    else
    {
        printf("お酒は飲めません\n");
    }

    return 0;
}