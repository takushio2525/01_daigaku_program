
#include <stdio.h>

void renzoku(int number)
{
    for (int i = 0; i < number; i++)
    {
        printf("#");
    }
}

void renzokuc(int number, char ch)
{
    for (int i = 0; i < number; i++)
    {
        printf("%c", ch);
    }
}

void renzokuStr(int number, const char *str)
{
    for (int i = 0; i < number; i++)
    {
        printf("%s", str);
    }
}