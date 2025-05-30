#include <stdio.h>
int main(void)
{
    unsigned int num = 0b01111111111111111111111111111111;
    printf("10進数表示 %u\n", num);
    printf("16進数表示 %x\n", num);
    printf(" 8進数表示 %o\n", num);
}