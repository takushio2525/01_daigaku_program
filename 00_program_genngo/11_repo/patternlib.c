#include <stdio.h>

void printx(int flag)
{
    if (flag == 0)
        printf(" ");
    else
        printf("X");
}

void print_char_scaled(char c, int scale)
{
    for (int i = 0; i < scale; i++)
    {
        printf("%c", c);
    }
}

void printx_scaled(int flag, int scale)
{
    if (flag == 0)
    {
        print_char_scaled(' ', scale);
    }
    else
    {
        print_char_scaled('X', scale);
    }
}
