#include <stdio.h>
#include "patternlib.h"
int main(void)
{
    Config config;
    init_config(&config);
    const char *string = "ABC";
    printf("横方向表示\n");
    config.horizontal_flag = 1;
    show_str(string, config);
    printf("縦方向表示\n");
    config.horizontal_flag = 0;
    show_str(string, config);
    printf("拡大表示\n");
    config.scale = 2;
    show_str(string, config);
    printf("色付き表示\n");
    config.scale = 1;
    config.color_flag = 1;
    config.color = 2;
    show_str(string, config);
    printf("フォント変更表示\n");
    config.color_flag = 0;
    config.disp_char = '#';
    show_str(string, config);
    return 0;
}