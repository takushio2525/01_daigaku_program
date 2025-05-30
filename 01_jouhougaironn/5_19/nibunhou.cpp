#include <stdio.h>
#include <math.h>
int main()
{
    double a = 0;
    double b = 1.0;
    double c = (a + b) / 2;
    double e = 0.0001;
    while (1)
    {
        if (abs(c - a) < e)
        {
            printf("解は%f\n", c);
            break;
        }
        if (cos(c) - c * c < 0)
        {
            b = c;
        }
        else
        {
            a = c;
        }
        c = (a + b) / 2;
        printf("%f\n", c);
    }
    return 0;
}
