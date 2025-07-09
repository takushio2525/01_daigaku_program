#include <stdio.h>

void show2(char *str);

int main(void)
{
    char *string = "test";
    printf("main:%s\n", string);
    show2(string);
    printf("main:%s\n", string);
}

void show2(char *str)
{
    printf("show2:");
    while (*str != '\0')
    {
        printf("%c", *str++);
    }
    printf("\n");
}