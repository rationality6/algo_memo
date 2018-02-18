#include <stdio.h>
#include <stdlib.h>

int main()
{
  int num = 22;
  int *num_pointer = &num;
  printf("%p\n", num_pointer);

  int *num_pointer1 = malloc(sizeof(int));
  printf("%p\n", num_pointer1);

  free(num_pointer1);
  return 0;
}