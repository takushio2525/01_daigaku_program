#include <stdio.h>

int main(void)
{
    int pattern[][8][8] = {
        {{0, 0, 0, 1, 1, 0, 0, 0},
         {0, 0, 1, 0, 0, 1, 0, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 1, 1, 1, 1, 1, 1, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 0, 0, 0, 0, 0, 0, 0}},
        {{1, 1, 1, 1, 1, 1, 0, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 1, 1, 1, 1, 1, 0, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {0, 1, 0, 0, 0, 0, 1, 0},
         {1, 1, 1, 1, 1, 1, 0, 0},
         {0, 0, 0, 0, 0, 0, 0, 0}}};

    int len_x = sizeof(pattern[0][0]) / sizeof(int);
    int len_y = sizeof(pattern) / len_x / sizeof(int);
    int len_z = sizeof(pattern) / len_x / len_y / sizeof(int);
    printf("横：%d 縦：%d パターン数:%d\n", len_x, len_y, len_z);
    for (int y = 0; y < len_y; y++)
    {
        for (int x = 0; x < len_x; x++)
        {
            if (pattern[0][y][x] == 0)
                printf(" ");
            else
                printf("X");

        }

        printf("\n");
    }
}
