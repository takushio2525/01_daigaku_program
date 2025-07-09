#include <stdio.h>
#include "patternlib.h"
int main(void)
{
    int pattern[][8] = {
        {0, 0, 0, 1, 1, 0, 0, 0},
        {0, 0, 1, 0, 0, 1, 0, 0},
        {0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 1, 1, 1, 1, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0},
        {0, 0, 0, 0, 0, 0, 0, 0}};

    int len_x = sizeof(pattern[0]) / sizeof(int);
    int len_y = sizeof(pattern) / len_x / sizeof(int);
    printf("横：%d 縦：%d\n", len_x, len_y);
    for (int y = 0; y < len_y; y++)
    {
        for (int x = 0; x < len_x; x++)
        {
            printx(pattern[y][x]);
        }
        printf("\n");
    }
    return 0;
}