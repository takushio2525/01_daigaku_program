#include <stdio.h>
int main(void)
{
    // 要素数にNという名前を付ける
    enum
    {
        N = 5
    };

    // 要素数Nを使った配列の宣言
    int sales[N];

    // 配列数Nを使った繰り返し
    for (int i = 0; i < N; i++)
        scanf("%d", &sales[i]);
    for (int i = 0; i < N; i++)
        printf("%d ", sales[i]);
    puts("");
}