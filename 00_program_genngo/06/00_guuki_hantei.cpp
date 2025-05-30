#include <stdio.h>

int main() {
    int n;

    printf("値を入力してください\n");

    scanf("%d", &n);

    if (n % 2 == 0) {
        printf("偶数です\n");
    } else {
        printf("奇数です\n");
    }

    return 0;
}