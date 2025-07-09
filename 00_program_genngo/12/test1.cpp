#include<stdio.h>
int main() {
    int x=1000;
    int *y; // yを「int型へのポインタ変数」として宣言
    y = &x; // yにxのアドレスを代入

    printf("xのアドレス: %p\n", &x);
    printf("yに格納されているアドレス: %p\n", y); // y自体がアドレスを保持している
    printf("yが指す先の値: %d\n", *y); // yが指すアドレスにある値を取得
}