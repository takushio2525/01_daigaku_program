#define COL_SIZE 8
#define ROW_SIZE 8

void print_char(int flag, char _char);
void print_char_colored(int flag, char _char, int color);
void show_array_vertical_scaled(int array[][ROW_SIZE][COL_SIZE], char _char, int len_c, int scale, int color_flag);
void show_array_horizontal_scaled(int array[][ROW_SIZE][COL_SIZE], char _char, int len_c, int scale, int color_flag);
void show_array(int array[][ROW_SIZE][COL_SIZE], char _char, int len_c, int scale, int color_flag, int horizontal_flag);
int conv_ASCII(char _char);
int setFontArray(const char *str, int array[][ROW_SIZE][COL_SIZE]);

