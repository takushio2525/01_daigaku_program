#include <stdio.h>
#include "patternlib.h"

void print_char(int flag, char _char)
{
    if (flag == 0)
    {
        printf(" ");
    }
    else
    {
        if (_char == ' ')
        {
            printf("\e[47m%c\e[0m", _char);
        }
        else
        {
            printf("%c", _char);
        }
    }
}

void print_char_colored(int flag, char _char, int color)
{
    if (flag == 0)
        printf("\e[0m ");
    else
    {
        if (_char == ' ')
        {
            printf("\e[4%dm%c\e[0m", color, _char);
        }
        else
        {
            printf("\e[3%dm%c\e[0m", color, _char);
        }
    }
}

void show_array_vertical_scaled(int array[][ROW_SIZE][COL_SIZE], char _char, int len_c, int scale, int color_flag)
{

    for (int c = 0; c < len_c; c++)
    {

        for (int y = 0; y < ROW_SIZE * scale; y++)
        {
            for (int x = 0; x < COL_SIZE; x++)
            {
                for (int s = 0; s < scale; s++)
                {
                    if (color_flag)
                    {
                        print_char_colored(array[c][y / scale][x], _char, array[c][y / scale][x]);
                    }
                    else
                    {
                        print_char(array[c][y / scale][x], _char);
                    }
                }
            }
            printf("\n");
        }
    }
}

void show_array_horizontal_scaled(int array[][ROW_SIZE][COL_SIZE], char _char, int len_c, int scale, int color_flag)
{

    for (int y = 0; y < ROW_SIZE * scale; y++)
    {
        for (int c = 0; c < len_c; c++)
        {
            for (int x = 0; x < COL_SIZE; x++)
            {
                for (int s = 0; s < scale; s++)
                {
                    if (color_flag)
                    {
                        print_char_colored(array[c][y / scale][x], _char, array[c][y / scale][x]);
                    }
                    else
                    {
                        print_char(array[c][y / scale][x], _char);
                    }
                }
            }
        }
        printf("\n");
    }
}

void show_array(int array[][ROW_SIZE][COL_SIZE], char _char, int len_c, int scale, int color_flag, int horizontal_flag)
{
    if (horizontal_flag)
    {
        show_array_horizontal_scaled(array, _char, len_c, scale, color_flag);
    }
    else
    {
        show_array_vertical_scaled(array, _char, len_c, scale, color_flag);
    }
}