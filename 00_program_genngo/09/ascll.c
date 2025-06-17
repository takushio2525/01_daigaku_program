#include <stdio.h>
int main(void)
{
    puts("char code");
    for (unsigned char i = 32; i < 128; i++)
    {
        printf("%4c %4d %4x\n", i, i, i);
    }
}