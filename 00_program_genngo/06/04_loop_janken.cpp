#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    unsigned int myWinCount = 0;
    unsigned int cpuWinCount = 0;

    while (myWinCount < 10 && cpuWinCount < 10)
    {
        unsigned int myHand = 3;
        printf("現在のスコア: あなた %u 勝, コンピュータ %u 勝\n", myWinCount, cpuWinCount);
        printf("値を入力してください 0:グー　1:チョキ　2:パー\n");
        while (myHand > 2)
        {
            scanf("%d", &myHand);
            if (myHand > 2)
            {
                printf("入力値が不正です\n");
            }
        }

        char *hands[] = {"グー", "チョキ", "パー"};
        printf("あなたの手は %s です\n", hands[myHand]);
        srand((unsigned int)time(NULL));
        unsigned int computerHand = rand() % 3;
        printf("コンピュータの手は %s です\n", hands[computerHand]);
        if (myHand == computerHand)
        {
            printf("あいこです\n");
        }
        else if ((myHand == 0 && computerHand == 1) || (myHand == 1 && computerHand == 2) || (myHand == 2 && computerHand == 0))
        {
            printf("あなたの勝ちです\n");
            myWinCount++;
        }
        else
        {
            printf("あなたの負けです\n");
            cpuWinCount++;
        }
    }
    printf("最終のスコア: あなた %u 勝, コンピュータ %u 勝\n", myWinCount, cpuWinCount);
    printf("ゲームを終了します\n");
    return 0;
}