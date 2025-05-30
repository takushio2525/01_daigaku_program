#include <stdio.h>

int main()
{
    int n1, n2, n3;

    printf("値１を入力してください\n");
    scanf("%d", &n1);

    printf("値２を入力してください\n");
    scanf("%d", &n2);

    printf("値３を入力してください\n");
    scanf("%d", &n3);

    if (n1 >= n2 && n1 >= n3)
    {
        printf("最大値は %d です\n", n1);
    }
    else if (n2 >= n1 && n2 >= n3)
    {
        printf("最大値は %d です\n", n2);
    }
    else
    {
        printf("最大値は %d です\n", n3);
    }

    return 0;
}