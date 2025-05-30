#include <stdio.h>
int main(void)
{
    float f = 4294.777;
    printf("0.1=%f\n", f);
    printf("0.1=%.1f\n", f);
    printf("0.2=%.2f\n", f);
    printf("0.3=%.3f\n", f);
}