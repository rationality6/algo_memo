#include <stdio.h>

int factorial(int num)
{
  if (num == 1)
  {
    return num;
  }
  else
  {
    return num * factorial(num - 1);
  }
}

int main()
{
  int result = factorial(5);

  printf("%d", result);

  return 0;
}
