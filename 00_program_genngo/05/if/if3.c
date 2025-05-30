#include <stdio.h>
int main(void)
{
    int t;
    printf("温度： ");
    scanf("%d", &t);

    if (t > 30)
        puts("クーラー");
    else if (t < 20)
        puts("暖房");
    else
        puts("off");

    if (t > 30)
    {
        puts("クーラー");
    }
    else if (t < 20)
    {
        puts("暖房");
    }
    else
    {
        puts("off");
    }
}