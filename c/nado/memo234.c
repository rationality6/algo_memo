#include <stdio.h>

int main(void)
{
  int i = 0;
  int j = 0;
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