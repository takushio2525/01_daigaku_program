#include <stdio.h>

int main()
{

    while (1)
    {
        int number;
        printf("何列表示しますか？");
        scanf("%d", &number);
        for (int y = 0; y < number; y++)
        {
            for (int x = 0; x < y + 1; x++)
            {
                printf("#");
            }
            printf("\n");
        }
        printf("\n");
    }
}