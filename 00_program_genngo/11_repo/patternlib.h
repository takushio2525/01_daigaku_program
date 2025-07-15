#define COL_SIZE 8
#define ROW_SIZE 8

#define FONT_DATA_SIZE 64

typedef struct
{
    int scale;
    int horizontal_flag;
    int color_flag;
    int color;
    int array[FONT_DATA_SIZE][ROW_SIZE][COL_SIZE];
    char disp_char;
} Config;

void print_char(int flag, char dispChar);
void print_char_colored(int flag, char dispChar, int color);
void show_str_vertical_scaled(const char *str, Config config);
void show_str_horizontal_scaled(const char *str, Config config);
void show_str(const char *str, Config config);
void init_config(Config *config);
int conv_ASCII(char _char);
void setFontArray(int array[FONT_DATA_SIZE][ROW_SIZE][COL_SIZE]);
void setFontArray_manual(int setData[FONT_DATA_SIZE][ROW_SIZE][COL_SIZE], Config config);