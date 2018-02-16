#include <stdio.h>

int main(void)
{
  int i = 1;
  int j = 1;
  while (i < 10)
  {
    while (j < 10)
    {
      printf("%d * %d = %d \n", i, j, i * j);
      j++;
    }
    i++;
  }

  return 0;
}