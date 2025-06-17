#include <stdio.h>
#include "renzoku/renzoku.h"

int main(void)
{
   for (int i = 0; i < 10; i++)
   {
      renzokuc(i, '$');
      printf("\n");
   }
}