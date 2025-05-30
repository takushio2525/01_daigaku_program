#include <stdio.h>
#include <math.h>

#define F cos(x) - (x *x)
#define FD -sin(x) - (2 * x)

int main()
{
    double x = 1.0;

    while (1)
    {
        double x1 = x - ((F) / (FD));
        if (abs(x1 - x) < 0.0001)
        {
            printf("解は%f\n", x1);
            break;
        }
        else
        {
            x = x1;
            printf("%f\n", x);
        }
    }
    return 0;
}
