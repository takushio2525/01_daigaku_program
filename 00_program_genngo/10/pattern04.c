#include <stdio.h>
#define SCALE 2

int main(void)
{
    int pattern[][8] = {
        {0, 1, 1, 1, 1, 1, 1, 0},
        {0, 3, 3, 7, 0, 3, 0, 0},
        {3, 3, 3, 0, 0, 0, 3, 0},
        {0, 1, 4, 1, 1, 4, 0, 0},
        {1, 1, 4, 4, 4, 4, 1, 0},
        {7, 1, 1, 4, 4, 4, 1, 7},
        {0, 4, 4, 4, 0, 4, 4, 0},
        {3, 3, 3, 0, 0, 3, 3, 3}};

    int len_x = sizeof(pattern[0]) / sizeof(int);
    int len_y = sizeof(pattern) / len_x / sizeof(int);
    printf("横：%d 縦：%d\n", len_x, len_y);

    for (int y = 0; y < len_y * SCALE; y++)
    {
        for (int x = 0; x < len_x * SCALE; x++)
        {
            printf("\e[4%dm ", pattern[y / SCALE][x / SCALE]);
        }
        printf("\e[0m\n");
    }
}