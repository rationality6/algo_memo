#include <stdio.h>
#include <string.h>
#include <math.h>

int data_types()
{
  printf("Storage size for in : %d \n", sizeof(int));
  return 0;
}

int main()
{
  char cset[] = "foobar";
  printf("%s\n", cset);

  for (int i = 0; i < (sizeof(cset) / sizeof(cset[0])) - 1; i++)
    printf("%c", cset[i]);

  char str[12] = "Hello";
  printf("%s\n", str);
  printf("%ld", sizeof(str) / sizeof(str[0]));

  // char names[][] = {"foo", "bar"};
  data_types();

  return 0;
}
