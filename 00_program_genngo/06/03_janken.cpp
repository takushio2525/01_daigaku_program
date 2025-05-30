#include <stdio.h>
#include <stdlib.h> // rand関数とsrand関数を使用するために必要
#include <time.h>   // time関数を使用するために必要

int main()
{
    unsigned int myHand;

    printf("値を入力してください 0:グー　1:チョキ　2:パー\n");
    scanf("%d", &myHand);
    if (myHand > 2)
    {
        printf("入力値が不正です\n");
        return 1;
    }
    char *hands[] = {"グー", "チョキ", "パー"};
    char *hantei[3][3] = {
        {"あいこ", "あなたかち", "あなたまけ"},
        {"あなたまけ", "あいこ", "あなたかち"},
        {"あなたかち", "あなたまけ", "あいこ"}};
    printf("あなたの手は %s です\n", hands[myHand]);
    srand((unsigned int)time(NULL));        // 乱数のシードを現在の時刻で初期化
    unsigned int computerHand = rand() % 3; // ここではコンピュータの手をランダムに決定
    printf("コンピュータの手は %s です\n", hands[computerHand]);
    printf(" %s です\n", hantei[myHand][computerHand]);
    printf("ゲームを終了します\n");
    return 0;
}