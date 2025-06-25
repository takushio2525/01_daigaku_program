#include <stdio.h>

int main(void)
{
    u_int16_t pattern[][16] = {
        {0x0008,
         0x0030,
         0x1fc0,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x7fff,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080},
        {0x0210,
         0x7fff,
         0x0210,
         0x0490,
         0x3ffe,
         0x0490,
         0x04f0,
         0x0400,
         0x07fc,
         0x0080,
         0x7fff,
         0x01c0,
         0x02a0,
         0x0c98,
         0x7087,
         0x0080},
        {0x0000,
         0x0000,
         0x3ffe,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x7fff,
         0x0000,
         0x0000},
        {0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x0080,
         0x7fff,
         0x0080,
         0x0080,
         0x0140,
         0x0140,
         0x0220,
         0x0220,
         0x0410,
         0x0808,
         0x1004,
         0x6003}};

    int len_y = sizeof(pattern[0]) / sizeof(u_int16_t);
    int len_x = sizeof(u_int16_t) * 8;
    int len_z = sizeof(pattern) / sizeof(u_int16_t) / len_y;
    printf("横：%d 縦：%d 文字数：%d\n", len_x, len_y, len_z);
    for (int z = 0; z < len_z; z++)
    {
        for (int y = 0; y < len_y; y++)
        {
            int mask = 0x8000;

            for (int x = 0; x < len_x; x++)
            {

                if ((pattern[z][y] & mask) == 0)
                    printf(" ");
                else
                    printf("X");

                mask = mask >> 1;
            }
            printf("\n");
        }
        printf("\n");
    }
}