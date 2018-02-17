#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int random_gen(int t)
{
  srand(t);
  int random_number = rand() % 3 == 0;
  return random_number % 3;
}

int subtract(int num, int num1)
{
  return num - num1;
}

int func_with_params(int num0, int num1, int num2)
{
  return num0 + num1 + num2;
}

int main()
{
  int random_number = random_gen(time(NULL));

  printf("foo %d", random_number);
  int val = func_with_params(1, 2, 3);
  printf("ff %d ff \n", val);
  printf("%d", subtract(10, 5));
  printf("%d", subtract(9, 2));

  return 0;
}
